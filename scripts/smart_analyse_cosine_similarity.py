#from gensim import corpora, models, similarities
import logging
import os
import re
import sys
import pandas as pd
# Scikit Learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import gensim
from gensim.matutils import softcossim 
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess

'''
# Analyse docs using Gensim Cosine Similarity
https://www.machinelearningplus.com/nlp/cosine-similarity/

Check for and display usage message
run .\scripts\python smart_analyse_cosine_similarity.py data
OR
python incubator\smart_analyse_cosine_similarity.py data
'''

# Main

# Set Logging level
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# Download the FastText model
print("Loading Fasttext model")
fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')

# Global variables
error_list = []
doc_names=[] # for holding names
documents=[] # for holding docs

#Setup the filter for only alphanumeric characters
pattern = re.compile('[\W_]+')


####################################
# Helper Classes
# Process file
def process_file(entry):

   # add the file to the entry 
   this_document=""

   #Actually load the docs as a corpus
   print ("Loading to corpus ... "+entry.path)

   try:
       for line in open(input_file_name, 'r', encoding="utf8"): 
           #convert to alphanumeric
           line =pattern.sub(' ', line)
           this_document = this_document + line

       documents.append(this_document)
       doc_names.append(pattern.sub('', entry.path))

   except UnicodeDecodeError:
        print("handled error")

'#######################################################'

if (len(sys.argv) != 2):    # arg 0 is script name
    print("\n=====")
    print("Smart")
    print("=====\n")
    print("Analyse documents based on cosine similarity\n")
    print("Usage:")
    print("python smart_analyse_cosine_similarity.py name_of_directory")
    sys.exit()

# Load Args into variables
input_dir_name = sys.argv[1]
print("Loading files from Directory:"+input_dir_name)

# Scan through documents
documents = []
for entry in os.scandir(input_dir_name):

    input_file_name = entry.path

    if entry.is_dir():
        print("Skipping Directory:"+input_file_name)
        continue

    if input_file_name[-4:].lower() != ".txt":
        print("Skipping non TXT file:"+input_file_name)
        continue

    # Process the file
    print("Processing file ... "+entry.path)
    process_file(entry)

    # Output results
    if(len(error_list)!=0):
        print("\n The following files had errors and were not processed:")
        print(error_list)

# Create the Document Term Matrix
count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(documents)

# Convert Sparse Matrix to Pandas Dataframe if you want to see the word frequencies.
print("Generating sparse Matrix of term frequencies")
doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names())


#compute the cosine similarity
print("Generating cosine similarity")
df_consine_sim= cosine_similarity(df, df)

#add the names ot this
df['file_name']=doc_names
df.set_index('file_name')

#Output as XL file
print("Outputting results as XL")
writer = pd.ExcelWriter('smart_Cosine_Similarity_Output.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

print("completed")
