#from gensim import corpora, models, similarities
import logging
#import docx
import sys
import os
import io
import textract
import PyPDF2
#import win32com.client
#import subprocess
import scripts.dao.Node

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#===============================================
# 'get text out of pretty much any file'
#===============================================

'''
class Extractor(object):
    

    #Process a PDF file
    
    

    #process using doc to
    def z_remove_processDocTo(self,entry,prev_dir,input_file_name,output_file_name):

        print("Processing DOC file using docto:"+entry.path)
        path_to_docto=prev_dir+"\\lib\\docto.exe"
        print("guessing that docto.exe is located in: "+path_to_docto)
                
        sub_command =path_to_docto+' -F "'+input_file_name+'" -O "'+output_file_name+'" -T wdFormatText'
        print("excuting: "+sub_command)
        subprocess.call(sub_command)
'''



#===============================================
# Extract text from docs in directory provided
#===============================================
class Walker (object):
    
    def processPDF(self,entry)->str:

        content = ""
        pdf = PyPDF2.PdfFileReader(entry.path, "rb")
        for i in range(0, pdf.getNumPages()):
            content += pdf.getPage(i).extractText() + " \n"
            content = " ".join(content.replace(u"\xa0", u" ").strip().split())
        return content
     
    
    def processTextTract(self,input_file_name)->str:
        
        print("Converting "+input_file_name+" to text")
        text = textract.process(input_file_name)
        return text

    # walk the directory tree

    def extract_dir(self, input_dir_name, dump_to_file=False)   :
       
        #Handle to the thing that does the text extractor
        node_list = []

        for entry in os.scandir(path=input_dir_name):
            
            #reset the contents
            text_contents=""

            # these files names give a .\filename - hence we drop the first two characters
            #input_file_name=entry.path[2:]
            input_file_name=entry.path
            output_file_name=input_file_name+".txt"

            if entry.is_dir():
                print("Skipping Directory:"+entry.path)
                continue

            elif os.path.isfile(output_file_name):
                print("Skipping as Output file already exists:"+output_file_name)
                continue
            
            elif input_file_name[-4:].lower() == ".pdf":
                text_contents=self.processPDF(entry)

            else:   
                #write everything else to interim text file
                print("trying to process file:"+input_file_name)
                text_contents=self.processTextTract(input_file_name)
            
            #### check what we should do with this
            if(dump_to_file):
                f = open(output_file_name,'w', encoding='utf-8')
                f.write(text_contents)
                f.close()
            else:
                doc1 = scripts.dao.Node.DocumentNode()
                doc1.filename ="filename"
                doc1.contents =text_contents
                node_list.append(doc1)
                        
        return node_list
'''            # TODO - drop these back in or refactor out  
                
            elif input_file_name[-4:].lower() == ".doc":
                text_contents=my_extractor.processDocTo(entry,prev_dir,input_file_name)
                
            elif input_file_name[-4:].lower() == ".txt":
                print("Skipping TXT file:"+entry.path)'''


#==================================================
# simple code to run / test class from command line
#==================================================
if __name__ == '__main__':
    
    # Check for and display usage message
    if (len(sys.argv)==1):    # arg 0 is script name
      
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

    # Delegate to the walker object
    my_walker = Walker()
    my_walker.extract_dir(input_dir_name, True)

    #restore previous working directory
    os.chdir(prev_dir)
    print("Restored working directory to: "+os.getcwd())

    