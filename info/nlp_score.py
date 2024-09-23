'''
Score clients based on Natural Language Processing of file contentss
'''
import logging
import os

from pprint import pprint
from collections import defaultdict

from extract import text_extract
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

# Constants
# CLIENT_NLP_SCORE="NLP_SCORE"

def nlp_score_company_files(list_of_files:list)->list:
    ''' 
    walk a list of files and score 
    :param list_of_files - python list of files to score
    :return list of scores, one per file
    :rtype integer
    '''

    nlp_score_total=[]

    for this_file in list_of_files:
        
        score = nlp_score_file(this_file)
        logging.debug("Score:"+str(score)+" for "+this_file)

        if(score!=0):
            nlp_score_total.append(score)
        

    return nlp_score_total
        

def nlp_score_file(this_file_name:str)->float:
    ''' 
    Score sentiment postive or negative in this file

    Scoring based on https://github.com/cjhutto/vaderSentiment 
    @param this_file_name to score
     '''

    text= text_extract.read_text_from_file(this_file_name)

    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 

    #Carry out the scoring
    sentiment_dict = sid_obj.polarity_scores(text) 

    '''
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    '''

    #calc net score
    calc_score = (sentiment_dict['pos']-sentiment_dict['neg'])*100
    calc_score = round(calc_score, 2)

    print(f"Text Overall Rated As:{calc_score}") 
  
    #return the score
    return calc_score

        

