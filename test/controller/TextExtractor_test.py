import unittest
import scripts.dao.Config
import scripts.dao.Loader
import scripts.dao.Node


class Document_loader_test (unittest.TestCase):
    
    def setUp(self):
        self.pre_config = scripts.dao.Config.SmartConfig("config.ini")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 
    def test_text_extraction(self):
        self.fail("Test not yet implemented")

    
    def test_walker(self):
        self.fail("Test not yet implemented")



if __name__ == '__main__':
    unittest.main()