import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from data import client_dto

def export_data_frame(dataframe:pd.DataFrame,filename:str):
    '''
    exporta a dataframe as an excel file

    :param dataframe to export
    :param filename to export it to
    '''
    writer = ExcelWriter(filename)
    dataframe.to_excel(writer,'Sheet1',index=False)
    writer.save()
    print("Output saved in Excel file:"+filename)

def convert_list_dto_to_dataframe(clients:list)-> pd.DataFrame:
    '''
    Convenience method - loop through list and convert
    '''
    #output information holder
    output_df = pd.DataFrame()

    for this_client in clients:
        this_df = convert_dto_to_dataframe(this_client)
        output_df.add(this_df)

    return(output_df)


def convert_dto_to_dataframe(dto:client_dto.ClientData) -> pd.DataFrame:
    '''
    flatten a client DTO (cells containing list) into a simple table

    e.g. given a client DTO (which is a dictionary key,value) where vale = [a list]
    Convert the DTO to multiple lines (and fill in the blanks)

    Example given 
    NAME, DAYS_SINCE_LAST_UPDATE,ENGAGEMENT_SCORE,FILES	
    Acme corp, [92.14, 92.14, 91.95],8.91,['file1','file2','file3']

    it would generate
    NAME, DAYS_SINCE_LAST_UPDATE,ENGAGEMENT_SCORE,FILES	
    Acme corp, 92.14,8.91,'file1'
    Acme corp, 92.14,8.91,'file2'
    Acme corp, 91.95,8.91,'file3'

    This depends on 
    a) Python lists maintaining order
    b) when we a generating the sub lists, that we always walk over the files in the same order
    c) if one of the lists is longer than the other, an excpetion will be thrown

    :param dto to convert - expects it to have a get_dictionary method
    :return pandas dataframe with same data, but 'squared off'
    '''
    #output information holder
    output_df = None

    #info we need to discover about our dto object
    max_list_length=1
    keys_with_str=[]
    keys_with_list=[]

    #first pass through dictionary - identify single value and lists
    for key, value in dto.get_dictionary().items():
        print(key, value, type(value))
        if (isinstance(value,list)):
            keys_with_list.append(key)

            if(max_list_length==1):
                max_list_length=len(value)
        else:
            keys_with_str.append(key)

    print(f"\nFound info\n listsize:{max_list_length} lists:{keys_with_list} strings:{keys_with_str}\n\n")
    
    #use this information to create dataframe
    for line_num in range(max_list_length):

        this_names=[]
        this_line=[]

        # loop through and add strings - same value every time
        for key in keys_with_str:
            this_names.append(key)
            this_line.append(dto.get_dictionary().get(key))

        # loop thorugh and add lists 
        for key in keys_with_list:
            this_names.append(key)
            this_line.append(dto.get_dictionary().get(key)[line_num])

        #firsttime here - create output using names

        if(output_df==None):
            output_df = pd.DataFrame(this_line,columns=this_names)

        #basic add of information
        output_df = output_df.append(this_line)

    return output_df