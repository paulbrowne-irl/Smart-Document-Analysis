import unittest
import scripts.dao.Config
import scripts.dao.DocumentLoader
import scripts.model.DocumentNode


class Document_loader_test (unittest.TestCase):
    
    def setUp(self):
        self.pre_config = scripts.dao.Config.SmartConfig("config.ini")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 
    def test_db_connection(self):
        
        docLoader = scripts.dao.DocumentLoader.DocumentLoader(self.pre_config)
        num_result = docLoader.count_nodes()
        self.assertIsNotNone(num_result)
        self.assertGreaterEqual(num_result,0)

    def test_add_document(self):

        docLoader = scripts.dao.DocumentLoader.DocumentLoader(self.pre_config)

        num_result_before = docLoader.count_nodes()
        docLoader.add_document("some_filename","content of some madeup type",testdata=True)
        num_result_after = docLoader.count_nodes()
        self.assertEqual(num_result_before+1,num_result_after)
        

    def test_add_document_node(self):

        docLoader = scripts.dao.DocumentLoader.DocumentLoader(self.pre_config)

        myDoc = scripts.model.DocumentNode.DocumentNode()
        myDoc.filename="Another node-y filename.txt"
        myDoc.text="blah blah blah blah blah blah blah blah blah blah blah blah"
        myDoc.testdata=True

        num_result_before = docLoader.count_nodes()
        docLoader.add_document_node(myDoc)
        num_result_after = docLoader.count_nodes()
        self.assertEqual(num_result_before+1,num_result_after)
        
        
        



if __name__ == '__main__':
    unittest.main()