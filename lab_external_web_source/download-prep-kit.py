import nest_asyncio
from dpk_web2parquet.transform import Web2Parquet
from dpk_html2parquet.transform_python import Html2Parquet
import sys
import os
import shutil

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.lib import colors


nest_asyncio.apply()


#CONFIG
DOWNLOAD_HTML="downloads_html"
DOWNLOAD_PARQUET="downloads_parquet"
DOWNLOAD_MD="../downloads_pdf"
DEPTH=3
NUM_DOWNLOADS=2000


def download_html(filename):
    """
    Reads URLs from a text file, iterates through each URL,
    and prints them to the console.  Handles file not found errors.

    Args:
        filename (str): The name of the text file containing the URLs.
    """
    url_list=[]

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace, including newlines
                url = line.strip()
                # Process the URL (e.g., print, check validity, etc.)
                print(f"Processing URL: {url}")

                #  Add a basic check that the URL starts with http or https
                if not url.startswith("http://") and not url.startswith("https://"):
                    print(f"Warning: URL '{url}' does not start with 'http://' or 'https://'.")
                else:
                    print(f"Appending to list: URL '{url}'")
                    url_list.append(url)

    except FileNotFoundError:
        print(f"Error: File not found - '{filename}'.  Please ensure the file exists and the path is correct.", file=sys.stderr)
        #  It's good practice to exit with a non-zero status code on error.
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

                    
    #download these files
    Web2Parquet(urls= url_list,
            depth=DEPTH, 
            downloads=NUM_DOWNLOADS,
            folder=DOWNLOAD_HTML).transform()

def convert_html_to_parquet():
    
    print(f"Starting Conversion of HTML to Parquet")

    result = Html2Parquet(input_folder= DOWNLOAD_HTML, 
                output_folder= DOWNLOAD_PARQUET, 
                data_files_to_use=['.html'],
                html2parquet_output_format= "markdown"
                ).transform()

    if result == 0:
        print (f"✅ Operation completed successfully")
    else:
        raise Exception (f"❌ Operation  failed")
    

def convert_parquets_to_mds():
    """
    Scans a directory for .parquet files, sorts them, and converts them
    into multiple MD files. A new MD is created whenever the first 6
    characters of the parquet filename change.

    Args:
        directory_path (str): The path to the directory containing parquet files.

    Requires:
        pandas, pyarrow, reportlab libraries to be installed.
        (pip install pandas pyarrow reportlab)
    """

    pd.set_option("display.max_colwidth", 10000)

    directory_path= DOWNLOAD_PARQUET

   # --- 1. Validate Input Directory ---
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found or is not a valid directory: {directory_path}", file=sys.stderr)
        return

    print(f"Scanning directory: {directory_path}")

    # --- 2. Find and Sort Parquet Files ---
    parquet_files = []
    try:
        for filename in os.listdir(directory_path):
            if filename.lower().endswith(".parquet"):
                full_path = os.path.join(directory_path, filename)
                parquet_files.append(full_path)
    except OSError as e:
        print(f"Error accessing directory: {e}", file=sys.stderr)
        return

    if not parquet_files:
        print("No .parquet files found in the directory.")
        return

    parquet_files.sort()
    print(f"Found {len(parquet_files)} parquet files. Processing...")

    # --- 3. Process Files and Generate Markdown Files ---
    current_prefix = None
    current_md_content = "" # Accumulate markdown content as a string
    output_md_path = None
    group_counter = 0 # Renamed from pdf_counter

    for i, file_path in enumerate(parquet_files):
        filename = os.path.basename(file_path)
        if len(filename) < 10:
            print(f"Warning: Filename '{filename}' is shorter than 10 characters. Skipping prefix check for this file.")
            file_prefix = filename.split('.')[0]
        else:
            file_prefix = filename[:10]

        # --- Check if a new Markdown file needs to be started ---
        if file_prefix != current_prefix and current_prefix is not None:
            # Save the *previous* group's markdown content
            if current_md_content:
                 # Remove trailing horizontal rule if it exists before saving
                # if current_md_content.endswith("\n---\n\n"):
                #     current_md_content = current_md_content[:-5] # Remove last rule and newlines
               
                try:
                    print(f"Saving Markdown: {output_md_path}... length {len(current_md_content)}")
                    with open(output_md_path, 'w', encoding='utf-8') as f:
                        f.write(current_md_content)
                    print(f"Successfully created: {output_md_path}")


                except IOError as e:
                    print(f"Error writing Markdown file '{output_md_path}': {e}", file=sys.stderr)
                except Exception as e:
                    print(f"An unexpected error occurred while writing '{output_md_path}': {e}", file=sys.stderr)

            # Reset for the new group
            current_md_content = ""

        # --- Setup for a new Markdown group ---
        if file_prefix != current_prefix:
            current_prefix = file_prefix
            group_counter += 1
            output_filename = f"{current_prefix}_report_{group_counter}.md" # Changed extension
            output_md_path = os.path.join(directory_path, output_filename)
            print(f"\n--- Starting new Markdown group for prefix '{current_prefix}' -> {output_filename} ---")
            # Add title using Markdown H1
            current_md_content += f"# Report for Group: {current_prefix}\n\n"

        # --- Read Parquet File ---
        print(f"  Reading: {filename}...")
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
            print(f"  Error reading or processing parquet file '{filename}': {e}", file=sys.stderr)
            # Add error message to markdown
            current_md_content += f"**Error processing {filename}:**\n```\n{e}\n```\n\n"

        # --- Add Horizontal Rule after each file's content ---
        # This acts as a separator similar to PageBreak in PDF
        current_md_content += "---\n\n"


    # --- Save the very last Markdown group ---
    if current_md_content and output_md_path:
         # Remove trailing horizontal rule if it exists before saving
        if current_md_content.endswith("\n---\n\n"):
            current_md_content = current_md_content[:-5] # Remove last rule and newlines
        try:
            print(f"Saving final Markdown: {output_md_path}...")
            with open(output_md_path, 'w', encoding='utf-8') as f:
                f.write(current_md_content)
            print(f"Successfully created: {output_md_path}")
        except IOError as e:
            print(f"Error writing final Markdown file '{output_md_path}': {e}", file=sys.stderr)
        except Exception as e:
            print(f"An unexpected error occurred while writing final file '{output_md_path}': {e}", file=sys.stderr)


    print("\nProcessing complete.")


def main():
    """
    Main function to get the filename from the user and call the
    iterate_urls_from_file function.
    """
    filename="sources.txt"
    if len(sys.argv) != 2:
        
        print(f"no source filename give, defaulting to {filename}")
        # sys.exit(1)  # Exit if the correct number of arguments is not provided
    else:
        filename = sys.argv[1]


    # clear previous downloads
    shutil.rmtree(DOWNLOAD_HTML, ignore_errors=True)
    shutil.os.makedirs(DOWNLOAD_HTML, exist_ok=True)
    shutil.rmtree(DOWNLOAD_PARQUET, ignore_errors=True)
    shutil.os.makedirs(DOWNLOAD_PARQUET, exist_ok=True)
    shutil.rmtree(DOWNLOAD_MD, ignore_errors=True)
    shutil.os.makedirs(DOWNLOAD_MD, exist_ok=True)

    #download and transform
    download_html(filename)
    convert_html_to_parquet()
    convert_parquets_to_mds()

if __name__ == "__main__":
    main()





