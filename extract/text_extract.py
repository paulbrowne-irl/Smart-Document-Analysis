'''
Gather information from the text of files. Able to read text, and common office (word and excel) files
'''

import os
import logging
import os
import io
from pprint import pprint
from collections import defaultdict
import docx

import pyexcel

#module level vars
skip_file_types =["pdf","ppt","pptx"]
    
def read_text_from_file (this_file_name:str)->str:
    ''' read text from file - including common error handling
    :param this_file_name - file to read
    :return text from the file
    :rtype string
    '''

    #default return value
    text=""

    logging.debug("asked to nlp score:"+this_file_name)
    try:
        text= _read_text_from_file_no_error_handling(this_file_name)
    except IndexError as ie:
        logging.error ("Ignoring error on file:"+this_file_name)
        logging.error ("Most likely this is caused by an empty document or spreadsheet")
        logging.error (ie)
    
    return text


def _read_text_from_file_no_error_handling(this_file_name:str)->str:
    ''' Read the file as text - this has no error handling'''

    content=""
    this_file_name_lower=this_file_name.lower()

    #check if this is in the skip list (e.g. pdf)
    for suffix in skip_file_types:
       if this_file_name_lower.endswith(suffix):
           logging.info("match suffix "+suffix+" from skip list for file:"+this_file_name)
           return ""

    #check if we open as doc / docx
    if(this_file_name_lower.endswith("docx") or this_file_name_lower.endswith("doc")):
        print ("opening "+this_file_name+" as word file")

        #half file / half string to hold our data
        file_str = io.StringIO()

        gkzDoc = docx.Document(this_file_name)
        for paragraph in gkzDoc.paragraphs:
            file_str.write(paragraph.text)

        return file_str.getvalue()

    #check if we open as xls
    if(this_file_name_lower.endswith("xlsx") or this_file_name_lower.endswith("xls")):
        print ("opening "+this_file_name+" as xl file")

        #half file / half string to hold our data
        file_str = io.StringIO()

        #Open the main table
        my_dict = pyexcel.get_dict(file_name=this_file_name)

        for key, values in my_dict.items():
            file_str.write(key + " : " + ','.join([str(item) for item in values]))

        return file_str.getvalue()


    # Default - try opening as text
    print ("Default - opening "+this_file_name+" as plain text")
    with open(this_file_name, 'r', encoding="utf-8") as content_file:

        try:
            # Load content as lower case text
            content = content_file.read()
            content=content.lower()

            logging.info("loaded file content length:"+str(len(content)))

        except UnicodeDecodeError as e:
            logging.error("Ignoring UnicodeDecodeError - file not processed")
            logging.error(e)

    return content

   