import unittest

import scripts.model.Node


class Document_test (unittest.TestCase):
    
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
 

    def test_create_Company_Node(self):
        comp1 = scripts.model.Node.CompanyNode()
        comp1.name ="somename"
        comp1.company_id ="12345"

        comp2 = scripts.model.Node.CompanyNode()
        comp2.name ="somename"
        comp2.company_id ="12345"
        self.assertEquals(comp1,comp2)

        comp3 = scripts.model.Node.CompanyNode()
        comp3.name ="somename"
        comp3.company_id ="678910"
        self.assertNotEqual(comp1,comp3)



    def test_create_Company_related_docs(self):

        comp1 = scripts.model.Node.CompanyNode()
        comp1.name ="somename"
        comp1.company_id ="12345"
        comp1.testdata =True

        doc1 = scripts.model.Node.DocumentNode()
        doc1.filename ="filename"
        doc1.contents ="contents"
        doc1.testdata=True

        comp1.document.add(doc1)

if __name__ == '__main__':
    unittest.main()