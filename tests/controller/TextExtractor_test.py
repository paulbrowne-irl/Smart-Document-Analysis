import unittest
import scripts.controller.TextExtractor

class Document_loader_test (unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 
   
    def test_walker(self):
        extractor = scripts.controller.TextExtractor.Walker()
        my_nodes=extractor.extract_dir("test\\sample_docs")
        self.assertIsNotNone(my_nodes)
        self.assertGreater(len(my_nodes),0)



if __name__ == '__main__':
    unittest.main()