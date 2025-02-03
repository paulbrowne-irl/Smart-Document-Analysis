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
 
    def test_db_connection(self):
        
        docLoader = scripts.dao.Loader.DocumentLoader(self.pre_config)
        num_result = docLoader.count_nodes()
        self.assertIsNotNone(num_result)
        self.assertGreaterEqual(num_result,0)


    def test_add_document(self):

        docLoader = scripts.dao.Loader.DocumentLoader(self.pre_config)

        num_result_before = docLoader.count_nodes()
        docLoader.add_document("some_filename","content of some madeup type",testdata=True)
        num_result_after = docLoader.count_nodes()
        self.assertEqual(num_result_before+1,num_result_after)
        

    def test_add_remove_document_node(self):

        docLoader = scripts.dao.Loader.DocumentLoader(self.pre_config)
        num_result_before = docLoader.count_nodes()
        
        myDoc = scripts.dao.Node.DocumentNode()
        myDoc.filename="Another node-y filename.txt"
        myDoc.text="blah blah blah blah blah blah blah blah blah blah blah blah"
        myDoc.testdata=True

        
        docLoader.add_update_node(myDoc)
        num_result_after = docLoader.count_nodes()
        self.assertEqual(num_result_before+1,num_result_after)
        
        docLoader.remove_node(myDoc)
        num_result_after_after = docLoader.count_nodes()
        self.assertEqual(num_result_before,num_result_after_after)
        
        
    def test_add_remove_multiple_nodes(self):
    
        docLoader = scripts.dao.Loader.DocumentLoader(self.pre_config)
        num_result_before = docLoader.count_nodes()
        
        keyword1=scripts.dao.Node.KeywordNode()
        keyword1.word ="european"
        keyword1.testdata=True
        keyword2=scripts.dao.Node.KeywordNode()
        keyword2.word ="supply-chain"
        keyword2.testdata=True

        comp1 = scripts.dao.Node.CompanyNode()
        comp1.name ="Acme"
        comp1.company_id ="12345"
        comp1.testdata =True

        doc1 = scripts.dao.Node.DocumentNode()
        doc1.filename ="filename1"
        doc1.contents ="contents"
        doc1.testdata=True
        doc1.keyword.add(keyword1)
        doc1.keyword.add(keyword2)
        

        doc2 = scripts.dao.Node.DocumentNode()
        doc2.filename ="filename2"
        doc2.contents ="contents - blah blah"
        doc2.testdata=True
        doc2.keyword.add(keyword1)

        comp1.document.add(doc1)
        comp1.document.add(doc2)

       
        docLoader.add_update_node(comp1)
        num_result_after = docLoader.count_nodes()
        self.assertTrue(num_result_before+2>num_result_after)
        
        docLoader.remove_node(comp1)
        num_result_after_after = docLoader.count_nodes()
        self.assertEqual(num_result_before,num_result_after_after)
        

        



if __name__ == '__main__':
    unittest.main()