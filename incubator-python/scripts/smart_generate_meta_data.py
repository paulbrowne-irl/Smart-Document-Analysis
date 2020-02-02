from gensim import corpora, models, similarities
import logging
import pandas
import sys
import os
import io
import nltk
import gensim
from pprint import pprint
from gensim import corpora
from collections import defaultdict
import re, string
import csv
import nltk

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



####################################
# Helper Classes

#Corpus Iterator
class MyCorpus(object):
    def __iter__(self):
        for line in open('mycorpus.txt'):
        # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

####################################
# Main
# Sample usage  python .\scripts\smart_generate_meta_data.py .\table_word_knowledge.xlsx data .\output\output
#
# Check for and display usage message
if (len(sys.argv)!=4):    # arg 0 is script name
    print("\n=====")
    print("Smart Generate Meta Data")
    print("=====\n")
    print("Collate information from group of Text files\n")
    print("Usage:")
    print("python smart_generate_meta_data.py knowledge-base-name.xlsx name-of-directory-with_text_files output_file_base")
    print("\nOutput file names will be appended e.g. output.dict, output.corpus")
    sys.exit()

#Get the Args into variables
knowledge_base_name=sys.argv[1]
input_dir_name = sys.argv[2]
dictionary_output_file=sys.argv[3]+".dict"
corpus_output_file=sys.argv[3]+".corpus"
new_words_output_file=sys.argv[3]+".new_words.csv"



#Load knowledge base file
print("Loading XLS Knowledgebase, first sheet from "+knowledge_base_name)
xl_file=open(knowledge_base_name,'rb')
print(xl_file)
df_kb = pandas.read_excel(xl_file, sheet_name=0)
stop_df= df_kb[df_kb['stoplist'] == 'Y']
stop_list_from_kb=stop_df['keyword'].tolist()



#Set the stop words and make sure all keywords lowercase
print("loading stop words from knowledgbase and nltk stopword file")
stop_words=[]
for x in stop_list_from_kb:
    stop_words.append(x.lower())
stop_words.extend(nltk.corpus.stopwords.words('english'))

#Setup the filter for only alphanumeric characters
pattern = re.compile('[\W_]+')


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
    print ("Loading to corpus ... "+entry.path)

    try:
        for line in open(input_file_name, 'r', encoding="utf8"):
            
            #convert to alphanumeric
            line =pattern.sub(' ', line)
            documents.append(line)
    except UnicodeDecodeError:
        print("handled error")

print("Number of document loaded:"+str(len(documents)))



# Split document into words
# Sample from https://radimrehurek.com/gensim/tut1.html
# remove common words and tokenize
#stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stop_words]for document in documents]
print("Number of texts in documents:"+str(len(texts)))



# Removing words not in NLTK Corpus
english_words = set(nltk.corpus.words.words())
texts = [[token for token in text if token.lower() in english_words]
    for text in texts]

# remove words that appear only once
print("Removing words that only appear once")
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
    for text in texts]





#Generate Dictionary from Texts     
dictionary = corpora.Dictionary(texts)
dictionary.save_as_text(dictionary_output_file,sort_by_word=True)  # store the dictionary, for future reference
print("Saved Dictionary to:"+dictionary_output_file)



#Use this Dictionary to generate Corpus
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize(corpus_output_file, corpus)  # store to disk, for later use
print("Saved corpus to:"+corpus_output_file)



#Generate list of new words
print("Looking for words in Corpus not in Knowledge base")
all_words_in_kb = df_kb['keyword'].tolist() 
dict_words=dictionary.items()
new_words=[]
for x in dict_words:
    if x[1] not in all_words_in_kb:
        if not x[1].isdigit():
            new_words.append(x[1])

print("Saving "+str(len(new_words))+" new words to "+new_words_output_file)

with open(new_words_output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for val in new_words:
        writer.writerow([val])




