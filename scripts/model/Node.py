from py2neo.ogm import GraphObject, Label, Property, Related, RelatedTo

# Tutorial https://py2neo.org/v4/ogm.html
    


class DocumentNode(GraphObject):

    __primarykey__ = "filename"

    Document = Label()
    filename = Property()
    text = Property("text")
    testdata = Property()

    #company = Related("company","CONTAINS")


class CompanyNode(GraphObject):

    __primarykey__ = "company_id"

    company = Label()
    company_id = Property()
    name = Property()
    testdata = Property()

    document = Related(DocumentNode)