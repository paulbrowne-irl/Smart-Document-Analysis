#from gensim import corpora, models, similarities
import logging
import docx
import sys
import os
import io
import textract
import PyPDF2
import win32com.client
import subprocess

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

###############################################
# convert pdf to text
##############################################
def convertPdf2String(path):
      content = ""
      pdf = PyPDF2.PdfFileReader(path, "rb")
      for i in range(0, pdf.getNumPages()):
          content += pdf.getPage(i).extractText() + " \n"
          content = " ".join(content.replace(u"\xa0", u" ").strip().split())
      return content


#===============================================
# Extract text from docs in directory provided
#===============================================


# Check for and display usage message
if (len(sys.argv)==1):    # arg 0 is script name
    print("\n=====")
    print("SMaRt")
    print("=====\n")
    print("Extract text from PDF, PPT, Doc, Docx, XLS and other Docs\n")
    print("Usage:")
    print("python smart_extract_text.py name-of-directory-to-convert")
    sys.exit()

#Get the Args into variables
#print( "This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: " , str(sys.argv))
input_dir_name = sys.argv[1]

#workaround for docto conversion
prev_dir=os.getcwd()
os.chdir(input_dir_name)
print("Moved to working directory to facilitate Word Doc to: "+os.getcwd())

for entry in os.scandir():

    # these files names give a .\filename - hence we drop the first two characters
    input_file_name=entry.path[2:]
    output_file_name=input_file_name+".txt"

    if entry.is_dir():
        print("Skipping Directory:"+entry.path)
        continue

    if os.path.isfile(output_file_name):
        print("Skipping as Output file already exists:"+output_file_name)
        continue

    if input_file_name[-4:].lower() == ".pdf":
        print("Processing PDF file:"+entry.path)
        text= convertPdf2String(entry.path)
        f = open(output_file_name,'w', encoding='utf-8')
        f.write(text)
        f.close()
        continue
    
    if input_file_name[-4:].lower() == ".doc":
        print("Processing DOC file using docto:"+entry.path)
        path_to_docto=prev_dir+"\\lib\\docto.exe"
        print("guessing that docto.exe is located in: "+path_to_docto)
        
        sub_command =path_to_docto+' -F "'+input_file_name+'" -O "'+output_file_name+'" -T wdFormatText'
        print("excuting: "+sub_command)
        subprocess.call(sub_command)

        # doc to text call
        continue
    
    if input_file_name[-4:].lower() == ".txt":
        print("Skipping TXT file:"+entry.path)
        continue

    #write everything else to interim text file
    print("Converting "+input_file_name+" to text")
    text = textract.process(input_file_name)
    f = open(output_file_name,'wb')
    f.write(text)
    f.close()

#restore previous working directory
os.chdir(prev_dir)
print("Restored working directory to: "+os.getcwd())