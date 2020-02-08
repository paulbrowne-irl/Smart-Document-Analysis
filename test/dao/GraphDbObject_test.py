import unittest
import scripts.dao.Config
import scripts.dao.GraphDbObject


class Test_GraphdbObject (unittest.TestCase):
    
 
    def test_dbconnection(self):

       myConfig = scripts.dao.Config.SmartConfig("config.ini")
       db = scripts.dao.GraphDbObject.DB_Access_NeoModel(myConfig)

       query="CREATE (a:Greeting) SET a.message = $message RETURN a.message + ', from node ' + id(a)"
       params="test messge"

       self.assertIsNotNone(db.execute_cyper(query,params))

if __name__ == '__main__':
    unittest.main()