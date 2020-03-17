from py2neo.ogm import GraphObject, Label, Property, RelatedFrom


# Tutorial https://py2neo.org/v4/ogm.html
    

class DocumentNode(GraphObject):


    #filename: str
    #text: str

    __primarykey__ = "filename"

    document = Label()
    filename = Property()
    text = Property("text")
    testdata = Property()

    #actors = RelatedFrom("Person", "ACTED_IN")
    #directors = RelatedFrom("Person", "DIRECTED")
    #producers = RelatedFrom("Person", "PRODUCED")
