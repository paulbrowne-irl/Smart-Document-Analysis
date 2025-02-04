'''
Data transfer Object for gathering information about a single client
'''
from dataclasses import dataclass

@dataclass
class ClientData():
   
    '''
    Data transfer Object for gathering information about a single client
    '''
    
    # Constants
    _CLIENT_NAME="NAME"
    _CLIENT_FILES="FILES"
    _FILE_SIZES="FILE_SIZES"
    _NUMBER_OF_FILES="NUMBER_OF_FILES"
    _DAYS_SINCE_LAST_UPDATE="DAYS_SINCE_LAST_UPDATE"
    _SENTIMENT_SCORE="SENTIMENT_SCORE"
    _ENGAGEMENT_SCORE="ENGAGEMENT_SCORE"

    def __init__(self):
        
        #Dictionary that we add info to
        self._clients_info = {}

    def get_dictionary(self) ->dict:
        '''
        Get all the info we hold about a client
        :return info on a single client
        :rettype dictionary
        '''
        return self._clients_info
    
    def __str__(self):
        '''
        :return the clinet info we hold as a string
        :rettype string
        '''
        return str(self._clients_info)

    def set_name(self,name):
        '''
        settor method
        '''
        self._clients_info[ClientData._CLIENT_NAME]= name

    def get_name(self):
        '''
        gettor method
        '''
        return self._clients_info[ClientData._CLIENT_NAME]

    def set_filenames(self,files):
        '''
        settor method
        '''
        self._clients_info[ClientData._CLIENT_FILES]= files

    def get_filenames(self):
        '''
        gettor method
        '''
        return self._clients_info[ClientData._CLIENT_FILES]

    def set_file_sizes(self,file_sizes):
        '''
        settor method
        '''
        self._clients_info[ClientData._FILE_SIZES]= file_sizes

    def set_number_of_files(self,number_of_files):
        '''
        settor method
        '''
        self._clients_info[ClientData._NUMBER_OF_FILES]= number_of_files

    def set_days_since_last_update(self,days_since_last_update):
        '''
        settor method
        '''
        self._clients_info[ClientData._DAYS_SINCE_LAST_UPDATE]= days_since_last_update

    def get_days_since_last_update(self):
        '''
        gettor method
        '''
        return self._clients_info[ClientData._DAYS_SINCE_LAST_UPDATE]

    def set_engagement_score(self,engagement_score):
        '''
        settor method
        '''
        self._clients_info[ClientData._ENGAGEMENT_SCORE]= engagement_score

    def set_sentiment_score(self,sentiment_score):
        '''
        settor method
        '''
        self._clients_info[ClientData._SENTIMENT_SCORE]= sentiment_score


    