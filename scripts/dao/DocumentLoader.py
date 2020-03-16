import scripts.dao.Config

from neomodel import config
from neomodel import db
from neomodel import util

from py2neo import Graph 


# Read and write Documents from Neo4j
class DocumentLoader(object):

    def __init__(self, smart_config):

        # store the config for later
        self.smart_config=smart_config
       
    # execute query
    # return results, meta
    def execute_cyper(self, query,params):
        
        print("trying to connect to:"+self.smart_config.getDbConnectionString())
        db.set_connection(self.smart_config.getDbConnectionString())

         #setup the DB connection
        #db.DATABASE_URL =
        #db.DATABASE_URL="bolt://neo4j:password@localhost:7687"
        #db.DATABASE_URL="bolt://neo4j:neo4j@localhost:7687"
        
        # for standalone queries
        return db.cypher_query(query, params)


#Refactoring in progress
def add_document(self):

    #First parameter is the URL, the password  second is the username and third is 
    graph = Graph(password="password")
    #nodes = graph.nodes().get()
    print(graph.run("MATCH (n)  RETURN n").to_data_frame())
    # py2neo.authenticate( "localhost:7474" , "neo4j","password") 
    # graph= Graph("http://localhost:7474/db/data/") 

        
#Refactoring in progress
def merge_document(self):
    print("not yet implemented")


#Refactoring in progress
def delete_document(self):
    print("not yet implemented")

# simple code to run / test class from command line
if __name__ == '__main__':
    config = scripts.dao.Config.SmartConfig("../../config.ini")
    db = DocumentLoader(config)
    
