from py2neo.ogm import GraphObject, Label, Property, RelatedFrom


# Tutorial https://py2neo.org/v4/ogm.html
    

class CompanyNode(GraphObject):


    #filename: str
    #text: str

    __primarykey__ = "company_id"

    company = Label()
    company_id = Property()
    name = Property()
    testdata = Property()

    #actors = RelatedFrom("Person", "ACTED_IN")
    #directors = RelatedFrom("Person", "DIRECTED")
    #producers = RelatedFrom("Person", "PRODUCED")
