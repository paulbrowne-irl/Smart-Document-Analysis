'''
Score clients based on all known information about them
'''
import logging
import pprint

import extract.meta_extract

def score_all_clients(all_clients:list):
    '''
    scores all clients
    expects dictionary of company name, dictionary with attributes
    '''
    for client_name, value in all_clients.items():
        score_client(all_clients[client_name])

    return all_clients

def score_client(client_info)->float:
    '''
    gives the company and engagement score, based on individual info
    '''

    days_since = client_info.get_days_since_last_update()
    return score_engagement(days_since)

def score_engagement(list_days_since:list)->float:
    ''' return based on average of last 3 values'''

    #zero list check
    if len(list_days_since)==0:
        return 0

    #sort so we get 3 smallest values
    days_since=sorted(list_days_since)
    days_since = days_since[:3]

    #Average
    logging.debug("days since:")
    logging.debug(days_since)

    avg_days_since = sum(days_since) / len(days_since) 

    return 100 - avg_days_since

def rebase_list_one_hundred(list_to_rebase:list)->list:
    ''' rebase a list of numbers to one hundred. 
    e.g. 253 to 1100 gets moved to 100 (and all other numbers in proportion)
    :param list_to_rebase  
    :return adjustment needed
    :rtype long
    '''
    #zero list check
    if len(list_to_rebase)==0:
        return list_to_rebase
    

    list_to_rebase=sorted(list_to_rebase, reverse=True)
    biggest_number = list_to_rebase[1]

    print("Biggest Number:"+str(biggest_number))
    adjustment = 100/biggest_number


    return adjustment
