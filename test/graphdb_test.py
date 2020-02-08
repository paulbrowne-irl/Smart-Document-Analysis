import unittest
import scripts.Config
import scripts.GraphDb


class Test_Graphdb (unittest.TestCase):
    
 
    def test_dbconnection(self):
        
        myConfig = scripts.Config.SmartConfig("config.ini")
        print("trying to connect using "+str(myConfig))

        db = scripts.GraphDb.DB_Access(myConfig)
        self.assertIsNotNone(db.get_greeting("message"))


if __name__ == '__main__':
    unittest.main()