import nest_asyncio
from dpk_web2parquet.transform import Web2Parquet
from dpk_html2parquet.transform_python import Html2Parquet
import sys
import os
import shutil
import json

import pandas as pd
import logging
import pprint


# CONFIG
# Set to True if you want to loop over the URLs, otherwise runs once and exits
LOOP_FLAG = False
DOWNLOAD_HTML = "downloads_html"
DOWNLOAD_PARQUET = "downloads_parquet"
DOWNLOAD_MD = "downloads_md"
# Notebook lm only allows 50 total input sources, this allows to combine inputs into one file
COMBINE_X_WEBSITES_INTO_ONE_MD_FILE = 4
DEPTH = 2
NUM_DOWNLOADS = 2
PQ_COLS_SKIP = ["document_id", "size"]

MD_OUTPUT_FILE_BASE = "source_"
URL_SNAPHOT_JSON = "url_snapshot.json"


def get_dict_source_files(source_file_as_txt):
    """
    Reads URLs from a text file, iterates through each URL,
    and logs them to the console. Handles file not found errors.

    Args:
        source_file_as_txt (str): The name of the text file containing the URLs.

    Returns:
        dict: A dictionary where each URL is a key, and the value is False.
    """
    url_dict = {}

    try:
        with open(source_file_as_txt, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace, including newlines
                url = line.strip()
                # Process the URL (e.g., logger.info, check validity, etc.)
                logger.info(f"Processing URL: {url}")

                # Add a basic check that the URL starts with http or https
                if not url.startswith("http://") and not url.startswith("https://"):
                    logger.info(
                        f"Warning: URL '{url}' does not start with 'http://' or 'https://'.")
                else:
                    logger.info(
                        f"Adding to dictionary: URL '{url}' with value False")
                    url_dict[url] = False

    except FileNotFoundError:
        logger.error(
            f"Error: File not found - '{source_file_as_txt}'. Please ensure the file exists and the path is correct.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

    return url_dict


def convert_urls_to_md(url_dict):
    """
    Converts a list of URLs to markdown files.  This is a placeholder function
    and should be replaced with the actual implementation.

    Args:
        url_dict (url_dict): A list of URLs to be converted. url and true/false flag if processed
    """
    # clear interim folders
    shutil.rmtree(DOWNLOAD_PARQUET, ignore_errors=True)
    shutil.os.makedirs(DOWNLOAD_PARQUET, exist_ok=True)
    shutil.rmtree(DOWNLOAD_HTML, ignore_errors=True)
    shutil.os.makedirs(DOWNLOAD_HTML, exist_ok=True)
    # don't delete, just ensuire it exists
    shutil.os.makedirs(DOWNLOAD_MD, exist_ok=True)

    # --- 1 Download the next lot of urls ---
    counter = 0
    next_urls = []

    for key, value in url_dict.items():
        if value == False:

            # add to our next list
            next_urls.append(key)

            # Mark the URL as processed
            url_dict[key] = True
            counter += 1

            logger.info(f"Processing URL: {key}")
        else:
            logger.info(f"Skipping processed URL: {key}")

        # Check if the number of URLs exceeds the limit
        if counter >= COMBINE_X_WEBSITES_INTO_ONE_MD_FILE:
            break

    # download these files
    logger.info(f"Starting Conversion of Web to Parquet")

    # for some reason that just outputs html files, not parquet
    Web2Parquet(urls=next_urls,
                depth=DEPTH,
                downloads=NUM_DOWNLOADS,
                folder=DOWNLOAD_HTML).transform()

    # convert html to parquet
    Html2Parquet(input_folder=DOWNLOAD_HTML,
                 output_folder=DOWNLOAD_PARQUET,
                 data_files_to_use=['.html'],
                 html2parquet_output_format="markdown"
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
    file_sources = set()
    current_md_content = ""  # Accumulate markdown content as a string

    # do the loop
    for file_path in parquet_files:  # was enumerate(parquet_files)
        logging.info(f"Processing file: {file_path}")
        filename = os.path.basename(file_path)

        # --- Read Parquet File ---
        logger.info(f"  Reading: {filename}...")

        # add first 8 letters to generate unque filename
        file_sources.add(filename[0:8])

        try:
            df = pd.read_parquet(file_path)
            # Add filename using Markdown H2
            current_md_content += f"## Data from Website: http://www.{filename[0:-8]}\n\n"

            # --- Convert DataFrame to Markdown Text ---
            if df.empty:
                current_md_content += "_(File contains no data)_\n\n"
            else:
                for col_name in df.columns:

                    if col_name in PQ_COLS_SKIP:
                        logging.debug(
                            f"  Skipping column '{col_name}' in file '{filename}'")

                    else:
                        # Add column name using Markdown H3
                        current_md_content += f"### {col_name}\n"

                        # Add column contents in a text code block
                        col_content_str = df[col_name].to_string(index=False)

                        current_md_content += f"```text\n{col_content_str}\n```\n\n"

        except Exception as e:
            logger.info(
                f"  Error reading or processing parquet file '{filename}': {e}", file=sys.stderr)
            # Add error message to markdown
            current_md_content += f"**Error processing {filename}:**\n```\n{e}\n```\n\n"

        # --- Add Horizontal Rule after each file's content ---
        # This acts as a separator similar to PageBreak in PDF
        current_md_content += "---\n\n"

    # --- 4 Save the MD file  ---
    if (len(file_sources) > 0):
        output_filename = MD_OUTPUT_FILE_BASE+''.join(file_sources)+".md"
        logger.info(f"MD Output filename: {output_filename}")

        output_md_path = os.path.join(DOWNLOAD_MD, output_filename)

        if current_md_content and output_md_path:
            # Remove trailing horizontal rule if it exists before saving
            if current_md_content.endswith("\n---\n\n"):
                # Remove last rule and newlines
                current_md_content = current_md_content[:-5]
            try:
                logger.info(f"Saving final Markdown: {output_md_path}...")
                with open(output_md_path, 'w', encoding='utf-8') as f:
                    f.write(current_md_content)
                logger.info(f"Successfully created: {output_md_path}")
            except IOError as e:
                logger.error(
                    f"Error writing final Markdown file '{output_md_path}': {e}", file=sys.stderr)
            except Exception as e:
                logger.error(
                    f"An unexpected error occurred while writing  file '{output_md_path}': {e}", file=sys.stderr)
    else:
        logger.error(
            f"Error: No valid sources found for file creation. Skipping file creation.")

    logger.info("\n Chunk Processing complete.")

    return next_urls


if __name__ == "__main__":
    """
    Main function to get the filename from the user and call the
    iterate_urls_from_file function.
    """
    # setup logging
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)

    # Set system level parameters
    master_source_file = "sources.txt"
    nest_asyncio.apply()
    pd.set_option("display.max_colwidth", 10000)

    # load sources
    if os.path.exists(URL_SNAPHOT_JSON):
        with open(URL_SNAPHOT_JSON, 'r') as f:
            url_dict = json.load(f)  # Load the entire JSON content
            if not isinstance(url_dict, dict):  # check if the data is a list

                logger.info(
                    f"Warning: File '{master_source_file}' did not contain a list. defaulting to {master_source_file}.")
                url_dict = get_dict_source_files(master_source_file)

    else:
        logger.info(
            f"Info: File '{master_source_file}' not found. defaulting to {master_source_file}.")
        url_dict = get_dict_source_files(master_source_file)

    if (len(url_dict) == 0):
        logger.info(f"Error: No URLs found in the file. Exiting.")
        sys.exit(1)

    # loop over the urls
    while (len(url_dict) > 0):
        # Process the URLs in chunks

        logger.info(f"Processing chunk remaining urls amount {len(url_dict)} ")
        url_dict = convert_urls_to_md(url_dict)

        # --- 5 snapshot the counter if we have to run again  ---
        with open(URL_SNAPHOT_JSON, 'w') as filehandle:
            json.dump(url_dict, filehandle)
            
        
        logger.info(f"remaining written to {URL_SNAPHOT_JSON}")
        pprint.pprint(url_dict)

        # break if set in config
        if (LOOP_FLAG == False):
            logger.info(f"Info: Config set not to loop . Exiting.")
            break

    
