'''
Utilities for converting files between different formats
'''
import os
from os.path import isdir
import shutil
import pandas as pd
from PyPDF2 import PdfFileReader, PdfFileMerger
from win32com import client
import win32api

def generate_tmp_output_filename(file_name:str,tmp_dir_name:str)->str:
    '''
    Generate the name of a suitable tmp output file name.
    Most often, it combines :param tmp_dir_name with :param file_name
    in a way that removes any '..', and converts to absolute pate
    :return Absolulte path to a 
    :rtype String
    '''
    #Convert tmp dir to absolute paths if needed
    if not(str(tmp_dir_name).startswith("C:")):
        tmp_dir_name=os.path.abspath(tmp_dir_name)

    #get file name
    output_name= tmp_dir_name+file_name+".pdf"

    print ("Generated output file name:"+output_name)

    return output_name


def delete_remake_dir(name_of_directory_to_recreate:str):
    '''
    Deletes then recreates a directory
    :para name of directory
    '''
    try:
        #os.remove(name_of_directory_to_recreate) 
        shutil.rmtree(name_of_directory_to_recreate)

    except FileNotFoundError:
        # we don't mind if its not there!
        pass                    


    #now create a directory
    os.mkdir(name_of_directory_to_recreate)
    
    print ("New empty dir:"+name_of_directory_to_recreate)


def convert_excel_file_to_pdf(input_file_name:str,output_file_name:str):
    '''
    Convert a single excel file to a pdf
    :param input_file_name to convert
    :param output_file_name to output to
    '''


    #Convert to absolute paths if needed
    if not(str(input_file_name).startswith("C:")):
        input_file_name=os.path.abspath(input_file_name)

    if not(str(output_file_name).startswith("C:")):
        output_file_name=os.path.abspath(output_file_name)


    #use Python on Wincom to manipulate Excel into opening file
    print("Trying to convert Excel:"+input_file_name +"\n to pdf:"+output_file_name)
    
    excel = client.DispatchEx("Excel.Application")
    excel.Visible = 0

    wb = excel.Workbooks.Open(input_file_name,ReadOnly=True)
    ws = wb.Worksheets[0]

    try:
        wb.SaveAs(output_file_name, FileFormat=57)
    except Exception as e:
        print ("Failed to convert")
        print (str(e))
    finally:
        wb.Close()
        excel.Quit()



def convert_word_file_to_pdf(input_file_name:str,output_file_name:str):
    '''
    Convert a word excel file to a pdf
    :param input_file_name to convert
    :param output_file_name to output to
    '''

    #Convert to absolute paths if needed
    if not(str(input_file_name).startswith("C:")):
        print("Input file was:"+input_file_name)
        input_file_name=os.path.abspath(input_file_name)
        print("converted to ABS path:"+input_file_name)

    if not(str(output_file_name).startswith("C:")):
        output_file_name=os.path.abspath(output_file_name)
        print("convert output file to ABS path")

    #Log what we are trying to do
    print("Trying to convert Word:"+input_file_name +"\n to pdf:"+output_file_name)

    #Open word via com and save as pdf
    word = client.Dispatch('Word.Application')
    word.Visible = False
    doc = word.Documents.Open(input_file_name)
    doc.SaveAs(output_file_name, FileFormat=17 ) # 17 = wdFormatPDF
    doc.Close()
    word.Quit()

def combine_pdf_documents(input_directory:str,output_pdf_filename:str):
    '''
    Combine all the pdf documents into the :param input_directory
    into the :param output_pdf_filename
    '''
    # create handle to output pdf
    output = PdfFileMerger()
    
    # get files in directory
    diskobjects = os.scandir(input_directory)
    print(diskobjects)

    #loop through and append these files
    for this_file in diskobjects:

        #check if dir
        if this_file.is_file:

            print("Appending pdf:"+str(this_file.path))
            pdf_file2 = PdfFileReader(this_file.path)
            output.append(pdf_file2)

    print("Generated pdf filename:"+output_pdf_filename)
    output.write(output_pdf_filename)
