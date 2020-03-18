import scripts.dao.Config
from typing import Final

from py2neo import Graph, Node

# Read and write Nodes from Neo4j
class DocumentLoader(object):

    #What we store the nodes under
    DOCUMENT_TYPE:Final = "Document"
    FILENAME_PROPERTY:Final = "filename"
    CONTENT_PROPERTY:Final = "content"
    TESTDATA_PROPERTY:Final = "testdata"
    

    #Queries
    CYPHER_COUNT_NODES:Final ="MATCH (N) return count(N) as count"

    def __init__(self, smart_config):

        
        #setup connection to DB via py2neo
        config_password = smart_config.getPassword()
        config_user= smart_config.getUser()
        config_host = smart_config.getHost()
        config_port = smart_config.getPort()

        print("Trying connection via py2neo using config:"+str(smart_config))
        self.graph = Graph(host=config_host, port=config_port, user=config_user,password=config_password)

       
    # count the number of nodes in a graph
    def count_nodes(self):
        
        df= self.graph.run(DocumentLoader.CYPHER_COUNT_NODES).to_data_frame()
        
        return int(df['count'][0])   

    #Add a document to the Graph by translating it to a note
    def add_document(self, filename, content,testdata=False):

        #First parameter is the URL, the password  second is the username and third is
        my_node = Node(DocumentLoader.DOCUMENT_TYPE,FILENAME_PROPERTY=filename, CONTENT_PROPERTY=content)

        #Mark if this test data
        if(testdata):
            my_node[DocumentLoader.TESTDATA_PROPERTY]=True

        self.graph.create(my_node)

    #Add a document to the Graph
    def add_node(self, node):

        self.graph.push(node)
    
    #delete a node
    def remove_node(self,node):
        self.graph.delete(node)

# simple code to run / test class from command line
if __name__ == '__main__':
    config = scripts.dao.Config.SmartConfig("../../config.ini")
    db = DocumentLoader(config)
    
