import unittest
import scripts.dao.Config

class Test_SmartConfig (unittest.TestCase):
 
    def setUp(self):
        
        self.loader = scripts.dao.Config.SmartConfig("config.ini")
        

    def test_load_config(self):

        myConfig = self.loader.getConfig()
        self.assertIsNotNone((myConfig.sections()))
        self.assertIsNotNone((myConfig.get("neo4j","password")))

    def test_readNeo4JValues(self):
    
       # self.assertEqual(self.loader.getConfig().get("neo4j","uri"),self.loader.getUri())

        #Test we are getting values back (differetn, not null)
        self.assertNotEqual(self.loader.getHost(),self.loader.getUser())
        self.assertNotEqual(self.loader.getHost(),self.loader.getPassword())
        self.assertNotEqual(self.loader.getPassword(),self.loader.getUser())

    def test_readURLConnect(self):
        self.assertIsNotNone(self.loader.getPort())
        self.assertNotEqual("",self.loader.getPort())
 
if __name__ == '__main__':
    unittest.main()