import unittest
import scripts.ConfigLoader

class Test_ConfigLoader (unittest.TestCase):
 
    def test_load_config(self):

        myLoader = scripts.ConfigLoader.ConfigLoader("config.ini")
        myconfig = myLoader.getConfig()
        self.assertIsNotNone((myconfig.sections()))
        self.assertIsNotNone((myconfig.get("neo4j","uri")))
        
if __name__ == '__main__':
    unittest.main()