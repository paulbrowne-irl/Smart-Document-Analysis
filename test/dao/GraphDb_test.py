import unittest
import scripts.dao.Config
import scripts.dao.GraphDb


class Test_Graphdb (unittest.TestCase):
    
 
    def test_dbconnection(self):
        
        myConfig = scripts.dao.Config.SmartConfig("config.ini")
        print("trying to connect using "+str(myConfig))

        db = scripts.dao.GraphDb.DB_Access_Cypher(myConfig)
        self.assertIsNotNone(db.get_greeting("message"))


if __name__ == '__main__':
    unittest.main()