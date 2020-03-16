import unittest
import scripts.model.Document


class Document_test (unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 

    def test_create_document_data_object(self):

        doc1 = scripts.model.Document.Document("filename","contents")
        doc2 = scripts.model.Document.Document("filename","contents")
        self.assertEquals(doc1,doc2)

        doc3 = scripts.model.Document.Document("filename","contents-completely different")
        self.assertNotEqual(doc1,doc3)

        

if __name__ == '__main__':
    unittest.main()