import scripts.dao.Config
from typing import Final

from py2neo import Graph, Node

# Read and write Documents from Neo4j
class DocumentLoader(object):

    #What we store the nodes under
    DOCUMENT_TYPE:Final = "DOCUMENT"
    FILENAME_PROPERTY:Final = "filename"
    CONTENT_PROPERTY:Final = "content"
    

    #Queries
    CYPHER_COUNT_NODES:Final ="MATCH (N) return count(N) as count"

    def __init__(self, smart_config):

        
        #setup connection to DB via py2neo
        config_password = smart_config.getPassword()
        print("Trying connection via py2neo using password:"+config_password)
        self.graph = Graph(password=config_password)


       
    # count the number of nodes in a graph
    def count_nodes(self):
        
        df= self.graph.run(DocumentLoader.CYPHER_COUNT_NODES).to_data_frame()
        #print(df)
        return int(df['count'][0])   

    #Refactoring in progress
    def add_document(self, filename, content,testdata=False):

        #First parameter is the URL, the password  second is the username and third is
        my_node = Node(DocumentLoader.DOCUMENT_TYPE,FILENAME_PROPERTY=filename, CONTENT_PROPERTY=content)

        self.graph.create(my_node)
    
        
    #Refactoring in progress
    def merge_document(self):
        raise ValueError("not yet implemented")


    #Refactoring in progress
    def delete_document(self):
        raise ValueError("not yet implemented")


# simple code to run / test class from command line
if __name__ == '__main__':
    config = scripts.dao.Config.SmartConfig("../../config.ini")
    db = DocumentLoader(config)
    
