#from gensim import corpora, models, similarities
import logging
import pandas as pd
import sys
import os
import io
from pprint import pprint
from collections import defaultdict
import re, string
import csv

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

####################################
# Helper Classes
# Process file
def process_file(entry):
   
    with open(entry.path, 'r', encoding="utf-8") as content_file:
        try:
            # Load content as lower case text
            content = content_file.read()
            content=content.lower()

             #Loop over our dataframe set
            for i, row in df_keywords.iterrows():
                search_string = str(row['keyword'])
                number_of_times_in_file = content.count(search_string)
                if(number_of_times_in_file>0):
                    output_list.append([entry.path,search_string,number_of_times_in_file])

            print("loaded file content length:"+str(len(content)))

        except UnicodeDecodeError as e:
            print("Ignoring UnicodeDecodeError - file not processed")
            print(e)
            error_list.append(entry.path)
           
        print("Number of entries now:"+str(len(output_list)))
        

####################################

# Main 
def main():

    # Check for and display usage message
    if (len(sys.argv)!=4):    # arg 0 is script name
        print("\n=====")
        print("Quick smart")
        print("=====\n")
        print("Summary of keyword count in text files\n")
        print("Suitable for display in Smart.xls)
        print("Usage:")
        print("python smart_analyse_file_keyword.py word_table name-of-directory-with_text_files output_file")
        sys.exit()

    #Get the Args into variables
    word_file_name=sys.argv[1]
    input_dir_name = sys.argv[2]
    output_file_name=sys.argv[3]

    #Other Variables
    output_list= [] #list columns=['file','keyword','count']
    error_list=[]

    #Load knowledge basd file
    print("Loading Keywords , first sheet from "+word_file_name)
    df_keywords = pd.read_excel(open(word_file_name,'rb'), sheet_name=0)

    #Scan through documents
    documents = []
    for entry in os.scandir(input_dir_name):

        input_file_name=entry.path

        if entry.is_dir():
            print("Skipping Directory:"+input_file_name)
            continue

        if input_file_name[-4:].lower() != ".txt":
            print("Skipping non TXT file:"+input_file_name)
            continue

        #Actually load the docs as a corpus
        print ("Processing file ... "+entry.path)
        process_file(entry)


    #Output results
    print("\n The following files had errors and were not processed:")
    print(error_list)

    print("Saving "+str(len(output_list))+" mapped words to "+output_file_name)

    with open(output_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output_list)

# for calling directly from the command line
if (__name__ == '__main__'):
    main()

