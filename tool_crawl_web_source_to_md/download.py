import nest_asyncio
from dpk_web2parquet.transform import Web2Parquet
from dpk_html2parquet.transform_python import Html2Parquet
import sys
import os
import shutil

import pandas as pd
import logging




#CONFIG
DOWNLOAD_HTML="downloads_html"
DOWNLOAD_PARQUET="downloads_parquet"
DOWNLOAD_MD="downloads_md"
COMBINE_X_WEBSITES_INTO_ONE_MD_FILE=4   # Notebook lm only allows 50 total input sources, this allows to combine inputs into one file
DEPTH=3
NUM_DOWNLOADS=2000
MD_OUTPUT_FILE_BASE="source_as_md"


def get_list_source_files(source_file_as_txt):
    """
    Reads URLs from a text file, iterates through each URL,
    and logger.infos them to the console.  Handles file not found errors.

    Args:
        filename (str): The name of the text file containing the URLs.
    """
    url_list=[]

    try:
        with open(source_file_as_txt, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace, including newlines
                url = line.strip()
                # Process the URL (e.g., logger.info, check validity, etc.)
                logger.info(f"Processing URL: {url}")

                #  Add a basic check that the URL starts with http or https
                if not url.startswith("http://") and not url.startswith("https://"):
                    logger.info(f"Warning: URL '{url}' does not start with 'http://' or 'https://'.")
                else:
                    logger.info(f"Appending to list: URL '{url}'")
                    url_list.append(url)

    except FileNotFoundError:
        logger.info(f"Error: File not found - '{filename}'.  Please ensure the file exists and the path is correct.", file=sys.stderr)
        #  It's good practice to exit with a non-zero status code on error.
        sys.exit(1)
    except Exception as e:
        logger.info(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

    return url_list
                    

def convert_urls_to_md(url_list):
    """
    Converts a list of URLs to markdown files.  This is a placeholder function
    and should be replaced with the actual implementation.
    
    Args:
        url_list (list): A list of URLs to be converted.
    """
    file_counter=0
  
    # Loop over all the URLs in the list
    while (len(url_list) > 0):

        # clear interim folders
        shutil.rmtree(DOWNLOAD_PARQUET, ignore_errors=True)
        shutil.os.makedirs(DOWNLOAD_PARQUET, exist_ok=True)
        shutil.rmtree(DOWNLOAD_HTML, ignore_errors=True)
        shutil.os.makedirs(DOWNLOAD_HTML, exist_ok=True)
        # don't delete, just ensuire it exists
        shutil.os.makedirs(DOWNLOAD_MD, exist_ok=True)

        #increment counter
        file_counter += 1

        # --- 1 Download the next lot of urls ---
        next_urls = url_list[:COMBINE_X_WEBSITES_INTO_ONE_MD_FILE]
        url_list = url_list[COMBINE_X_WEBSITES_INTO_ONE_MD_FILE-1:]

        #download these files
        logger.info(f"Starting Conversion of Web to Parquet")

        # for some reason that just outputs html files, not parquet
        Web2Parquet(urls= next_urls,
                depth=DEPTH, 
                downloads=NUM_DOWNLOADS,
                folder=DOWNLOAD_HTML).transform()
        
        # convert html to parquet
        result = Html2Parquet(input_folder= DOWNLOAD_HTML, 
               output_folder= DOWNLOAD_PARQUET, 
               data_files_to_use=['.html'],
               html2parquet_output_format= "markdown"
               ).transform()

        
        # Now scans a directory for .parquet files, sorts them, and converts them
        # into multiple MD files. 
    

        logger.info(f"Scanning directory: {DOWNLOAD_PARQUET}")

        # --- 2. Find and Sort Parquet Files ---
        parquet_files = []
        try:
            for filename in os.listdir(DOWNLOAD_PARQUET):
                if filename.lower().endswith(".parquet"):
                    full_path = os.path.join(DOWNLOAD_PARQUET, filename)
                    parquet_files.append(full_path)
                    logger.info(f"Found parquet file: {full_path}")
        except OSError as e:
            logger.info(f"Error accessing directory: {e}", file=sys.stderr)
            return

        if not parquet_files:
            logger.info("No .parquet files found in the directory.")
            return

        parquet_files.sort()
        logger.info(f"Found {len(parquet_files)} parquet files. Processing...")

        # --- 3. Process Files and Generate Markdown Files ---
        #current_prefix = None
        current_md_content = "" # Accumulate markdown content as a string
        output_md_path = None
        output_filename = f"{MD_OUTPUT_FILE_BASE}_{file_counter}.md" # Changed extension
        output_md_path = os.path.join(DOWNLOAD_MD, output_filename)

        # do the loop
        for i, file_path in enumerate(parquet_files):
            filename = os.path.basename(file_path)

            # --- Read Parquet File ---
            logger.info(f"  Reading: {filename}...")
            try:
                df = pd.read_parquet(file_path)
                # Add filename using Markdown H2
                current_md_content += f"## Data from: {filename}\n\n"

                # --- Convert DataFrame to Markdown Text ---
                if df.empty:
                    current_md_content += "_(File contains no data)_\n\n"
                else:
                    for col_name in df.columns:
                        # Add column name using Markdown H3
                        current_md_content += f"### {col_name}\n"

                        # Add column contents in a text code block
                        # wascol_content_str = df[col_name].to_string(index=False)
                        col_content_str = df[col_name].to_string(index=False)
                        
                        current_md_content += f"```text\n{col_content_str}\n```\n\n"

            except Exception as e:
                logger.info(f"  Error reading or processing parquet file '{filename}': {e}", file=sys.stderr)
                # Add error message to markdown
                current_md_content += f"**Error processing {filename}:**\n```\n{e}\n```\n\n"

            # --- Add Horizontal Rule after each file's content ---
            # This acts as a separator similar to PageBreak in PDF
            current_md_content += "---\n\n"


        # --- 4 Save the MD file  ---
        if current_md_content and output_md_path:
            # Remove trailing horizontal rule if it exists before saving
            if current_md_content.endswith("\n---\n\n"):
                current_md_content = current_md_content[:-5] # Remove last rule and newlines
            try:
                logger.info(f"Saving final Markdown: {output_md_path}...")
                with open(output_md_path, 'w', encoding='utf-8') as f:
                    f.write(current_md_content)
                logger.info(f"Successfully created: {output_md_path}")
            except IOError as e:
                logger.info(f"Error writing final Markdown file '{output_md_path}': {e}", file=sys.stderr)
            except Exception as e:
                logger.info(f"An unexpected error occurred while writing  file '{output_md_path}': {e}", file=sys.stderr)


    logger.info("\nProcessing complete.")



if __name__ == "__main__":
    """
    Main function to get the filename from the user and call the
    iterate_urls_from_file function.
    """
    # setup logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    # Set system level parameters
    filename="sources.txt"
    nest_asyncio.apply()
    pd.set_option("display.max_colwidth", 10000)


    if len(sys.argv) != 2:
        logger.info(f"no source filename give, defaulting to {filename}")
        # sys.exit(1)  # Exit if the correct number of arguments is not provided
    else:
        filename = sys.argv[1]


    # clear previous downloads

    #shutil.rmtree(DOWNLOAD_MD, ignore_errors=True)
    #shutil.os.makedirs(DOWNLOAD_MD, exist_ok=True)

    #download and transform
    url_list = get_list_source_files(filename)
    convert_urls_to_md(url_list)

    
    





