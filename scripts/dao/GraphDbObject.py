from neo4j import GraphDatabase
from neomodel import db
import scripts.dao.Config

#Sample class to interact with neo4j
#This class is for executing queries
class DB_Access_NeoModel(object):

    def __init__(self, config):

        # store the config for later
        self.config=config

        #setup the DB connection
        db myGraphDb = db()
        myGraphDb.setConnection("")   


# simple code to run / test class from command line
if __name__ == '__main__':
    config = scripts.dao.Config.SmartConfig("../../config.ini")
    db = DB_Access_NeoModel(config)
    
