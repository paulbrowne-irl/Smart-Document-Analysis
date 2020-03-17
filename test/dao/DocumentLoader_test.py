import unittest
import scripts.dao.Config
import scripts.dao.DocumentLoader


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

    def test_add_merge_delete_docuemnt(self):

        docLoader = scripts.dao.DocumentLoader.DocumentLoader(self.pre_config)

        num_result_before = docLoader.count_nodes()
        docLoader.add_document("some_filename","content of some madeup type",testdata=True)
        num_result_after = docLoader.count_nodes()
        self.assertEqual(num_result_before+1,num_result_after)
        
        
        #these will fail as not yet implented
        docLoader.merge_document()
        docLoader.delete_document()

if __name__ == '__main__':
    unittest.main()