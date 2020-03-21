from py2neo.ogm import GraphObject, Label, Property, Related

import scripts.model.DocumentNode

# Tutorial https://py2neo.org/v4/ogm.html
    

class DocumentNode(GraphObject):


    #filename: str
    #text: str

    __primarykey__ = "filename"

    document = Label()
    filename = Property()
    text = Property("text")
    testdata = Property()

    company = Related(scripts.model.CompanyNode,"CONTAINS")
