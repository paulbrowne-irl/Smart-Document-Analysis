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
path = '..'                                 # where we look for client info
skip_dir = 'z_scripts'                      # directories to ignore
output_dir='z_output'                       # where we will generate the output
start_output_file_name="client_handback_"    # the start of the combined file aname
tmp_dir='C:/tmp/'                           # a working directory that is safe to delete
header_template='templates/000-front.docx'  # a front page for our output
header_name_in_folder='000-front.pdf'       # when we convert front page pdf in directory, what we call it



''' Run an analysis of the files in directory marked path'''  
if __name__ == "__main__":
    # execute only if run as a script

    # if needed for logging later
    pp = pprint.PrettyPrinter(indent=4)
    
    # walk first level directories
    diskobjects = os.scandir(path)

    print("scanning path:"+path)    
    
    # Walk the top level (client) directory
    for entry in diskobjects :

        if entry.is_dir() and str(entry.name)!=skip_dir:
    
            # clear out any tmp output directory
            extract.convert.delete_remake_dir(tmp_dir)

            #Generate the front page for our output - into the tmp dir
            report.pdf_sumsher.generate_front_page(header_name_in_folder,header_template,tmp_dir)

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
                    output_name= extract.convert.generate_tmp_output_filename(name,tmp_dir)
                    
                    # word
                    if(this_file_name.endswith("docx") or this_file_name.endswith("doc")):
                        extract.convert.convert_word_file_to_pdf(this_file_name,output_name)
                        continue

                    # excel
                    if(this_file_name.endswith("xlsx") or this_file_name.endswith("xls")):
                        extract.convert.convert_excel_file_to_pdf(this_file_name,output_name)
                        continue

                    #everything else
                    print("Ignoring file:"+this_file_name)
                
                #once all documents converted, combine into one
                pdf_output_name=output_dir+"/"+start_output_file_name+client_name+".pdf"
                print("output client summary pdf to:"+pdf_output_name)
                extract.convert.combine_pdf_documents(tmp_dir,pdf_output_name)

        diskobjects.close

  

       

  