'''
Summarize a clients work into one PDF.

Loop through folders (assume each top folder contains one clinet) and sub folders
Converts Word, Excel etc to PDF
Combines all docs into PDF (sorted by alphabetical order)
'''
import pprint
import logging
import os
import sys

import extract.convert
import report.pdf_smusher

'''Module level variables - these are safe to edit'''
CLIENT_DOCS_PATH = '..'                                 # where we look for client info
SKIP_DIR = 'z_scripts'                      # directories to ignore
OUTPUT_DIR='output'                       # where we will generate the output
START_OUTPUT_FILE_NAME="client_handback_"    # the start of the combined file aname
TMP_DIR='C:/tmp/'                           # a working directory that is safe to delete
HEADER_TEMPLATE='templates/000-front.docx'  # a front page for our output
HEADER_NAME_IN_FOLDER='000-front.pdf'       # when we convert front page pdf in directory, what we call it



''' Run an analysis of the files in directory marked path'''  
if __name__ == "__main__":
    # execute only if run as a script

    # if needed for logging later
    pp = pprint.PrettyPrinter(indent=4)
    
    # walk first level directories
    diskobjects = os.scandir(CLIENT_DOCS_PATH)

    print("scanning path:"+CLIENT_DOCS_PATH)    
    
    # Walk the top level (client) directory
    for entry in diskobjects :

        if entry.is_dir() and str(entry.name)!=SKIP_DIR:
    
            # clear out any tmp output directory
            extract.convert.delete_remake_dir(TMP_DIR)

            #Generate the front page for our output - into the tmp dir
            report.pdf_sumsher.generate_front_page(HEADER_NAME_IN_FOLDER,HEADER_TEMPLATE,TMP_DIR)

            #capture name
            client_name=entry.name

            #create a new company object
            company_info={}

            #Walk each client directory           
            for root, directories, files in os.walk(entry.path, topdown=False):

                # Get file info
                for name in files:
                    
                    # create the output name
                    this_file_name= os.path.join(root, name).lower()
                    output_name= extract.convert.generate_tmp_output_filename(name,TMP_DIR)
                    
                    # word
                    if(this_file_name.endswith("docx") or this_file_name.endswith("doc")):
                        try:
                            extract.convert.convert_word_file_to_pdf(this_file_name,output_name)
                        except Exception as e:
                            print(f"Error converting {this_file_name}: {e}")
                        continue

                    # excel
                    if(this_file_name.endswith("xlsx") or this_file_name.endswith("xls")):
                        try:
                            extract.convert.convert_excel_file_to_pdf(this_file_name,output_name)
                        except Exception as e:
                            print(f"Error converting {this_file_name}: {e}")
                        continue

                    #everything else
                    print("Ignoring file:"+this_file_name)
                
                #once all documents converted, combine into one
                pdf_output_name=OUTPUT_DIR+"/"+START_OUTPUT_FILE_NAME+client_name+".pdf"
                print("output client summary pdf to:"+pdf_output_name)
                extract.convert.combine_pdf_documents(TMP_DIR,pdf_output_name)

        diskobjects.close





