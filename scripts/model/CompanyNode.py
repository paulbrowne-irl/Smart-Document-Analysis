from py2neo.ogm import GraphObject, Label, Property, Related

import scripts.model.DocumentNode

# Tutorial https://py2neo.org/v4/ogm.html
    

class CompanyNode(GraphObject):


    #filename: str
    #text: str

    __primarykey__ = "company_id"

    company = Label()
    company_id = Property()
    name = Property()
    testdata = Property()

    documents = Related(scripts.model.DocumentNode,"CONTAINS")