import configparser
import os

#Sample to load config details
class ConfigLoader(object):
    'Convenience class to load system configuration'

    def __init__(self, config_file_name=None):

        #set defaults on incoming argumenst
        if(config_file_name==None):
            config_file_name="config.ini"

        self.config = configparser.ConfigParser()
        self.config.read(config_file_name)
        print(self.config.sections())

    def getConfig(self):
        return self.config

# simple code to run / test class from command line
if __name__ == '__main__':
    config = ConfigLoader("config.ini").config
    print(os.getcwd())
    print(config.sections())
    print(config.get("neo4j","uri"))
