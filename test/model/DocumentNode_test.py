import unittest

import scripts.model.DocumentNode


class Document_test (unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 

    def test_create_Document_Node(self):
        doc1 = scripts.model.DocumentNode.DocumentNode()
        doc1.filename ="filename"
        doc1.contents ="contents"

        doc2 = scripts.model.DocumentNode.DocumentNode()
        doc2.filename ="filename"
        doc2.contents ="contents"
        self.assertEquals(doc1,doc2)

        doc3 = scripts.model.DocumentNode.DocumentNode()
        doc3.filename ="filename-dfferent"
        doc3.contents ="contents"
        self.assertNotEqual(doc1,doc3)

if __name__ == '__main__':
    unittest.main()