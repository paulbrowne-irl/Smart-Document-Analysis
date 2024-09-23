'''
Gather information from the meta data of files
'''
import os
import datetime
import logging
import pathlib

import data.client_dto

def gatherInformation(info_file_path:str,skip_dir:str) -> list:
    ''' Gather information from directory (and sub dires) as specificed in path 
    :param info_file_path - directory path to searp
    :param skip_dir = directories to skip
    :return List of ClientDTOs - client name, info on the client files
    :rtype List
    '''

    # save
    now = datetime.datetime.now()

    #List that we add info to 
    all_clients = []

    # walk first level directories
    diskobjects = os.scandir(info_file_path)
    
    for entry in diskobjects :
        
        if entry.is_dir() and str(entry.name)!=skip_dir:

            #create a new client object
            this_client=data.client_dto.ClientData()

            #capture name
            this_client.set_name(entry.name)

            #reset counters
            number_of_files=0;
            date_list=[]
            file_size_list=[]
            file_list=[]

            #Walk each client directory           
            for root, directories, files in os.walk(entry.path, topdown=False):

                # Get file info
                for name in files:
                    number_of_files+=1
                   
                    # Get time since last edit
                    this_file_name= os.path.join(root, name)
                    logging.info("Gathering Meta Data:"+this_file_name)

                    file_handle = pathlib.Path(this_file_name)
                    time_since_edit= now-datetime.datetime.fromtimestamp(file_handle.stat().st_mtime)
                    time_since_edit_days=round(time_since_edit.days+(time_since_edit.seconds/(60*24)),2)
                    date_list.append(time_since_edit_days)

                    #Get file and sizes
                    file_list.append(this_file_name)
                    file_size_list.append(round(os.path.getsize(file_handle)/1024,2))
            
            # save the gather info as into our client DTO
            this_client.set_filenames(file_list)
            this_client.set_file_sizes(file_size_list)
            this_client.set_number_of_files(number_of_files)
            this_client.set_days_since_last_update(date_list)

            all_clients.append(this_client)

        diskobjects.close

    return all_clients






