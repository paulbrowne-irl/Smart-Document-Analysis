'''
Get a snapshot of client engagement using documents the companies have provided.

Examples of information that we can leverage
* last updated date
* number of documents
* Sentiment analysis
'''
import pprint
import logging
from report import flatten
import pandas as pd

import info.score
import info.nlp_score
import extract.meta_extract


'''Module level variables - these are safe to edit'''
path = '..'
output_file_name = 'z_output\\output.xls'
skip_dir = 'z_scripts'

''' Run an analysis of the files in directory marked path'''  
if __name__ == "__main__":
    # execute only if run as a script

    # if needed for logging later
    pp = pprint.PrettyPrinter(indent=4)

    #gather the client info
    all_clients = extract.meta_extract.gatherInformation(path,skip_dir)

    # Loop through clients and add NLP Score
    for my_client in all_clients:

        #We use the name quite a bit
        client_name=my_client.get_name()

        #Get the files for this client
        list_of_files = my_client.get_filenames()

        # Do (Basic score)
        this_nlp_score= info.nlp_score.nlp_score_company_files(list_of_files)
        my_client.set_sentiment_score(this_nlp_score)

        # While we're at it
        #score for engagement
        logging.info("About to score client:"+client_name)
        client_engagement = round(info.score.score_client(my_client),2)
        my_client.set_engagement_score(client_engagement)

    
    # convert our dto object to a pandas dataframe
    output_df= flatten.convert_list_dto_to_dataframe(all_clients)

    # Output the data as excel
    flatten.export_data_frame(output_df,output_file_name)

 

    
        



