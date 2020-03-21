import unittest

import scripts.model.CompanyNode
import scripts.model.DocumentNode


class Document_test (unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 

    def test_create_Company_Node(self):
        comp1 = scripts.model.CompanyNode.CompanyNode()
        comp1.name ="somename"
        comp1.company_id ="12345"

        comp2 = scripts.model.CompanyNode.CompanyNode()
        comp2.name ="somename"
        comp2.company_id ="12345"
        self.assertEquals(comp1,comp2)

        comp3 = scripts.model.CompanyNode.CompanyNode()
        comp3.name ="somename"
        comp3.company_id ="678910"
        self.assertNotEqual(comp1,comp3)



    def test_create_Company_related_docs(self):
        comp1 = scripts.model.CompanyNode.CompanyNode()
        comp1.name ="somename"
        comp1.company_id ="12345"

        doc1 = scripts.model.CompanyNode.CompanyNode()
        doc1.filename ="filename"
        doc1.contents ="contents"
        doc1.testdata=True

        comp1.documents.add(doc1)

if __name__ == '__main__':
    unittest.main()