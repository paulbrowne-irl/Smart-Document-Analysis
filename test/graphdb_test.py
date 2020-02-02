import unittest
import scripts.GraphDb

class Test_Graphdb (unittest.TestCase):
    
 
    def test_dbconnection(self):
        self.assertTrue(True)
        db = scripts.GraphDb.DB_Access()
        self.assertIsNotNone(db.get_greeting("message"))


if __name__ == '__main__':
    unittest.main()