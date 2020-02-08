import scripts.dao.Config

from neomodel import config
from neomodel import db
from neomodel import util


#Sample class to interact with neo4j
#This class is for executing queries
class DB_Access_NeoModel(object):

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
        


# simple code to run / test class from command line
if __name__ == '__main__':
    config = scripts.dao.Config.SmartConfig("../../config.ini")
    db = DB_Access_NeoModel(config)
    
