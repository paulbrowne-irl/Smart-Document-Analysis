from neo4j import GraphDatabase

#Sample class to interact wiht neo4j
class HelloWorldExample(object):

    def __init__(self, uri=None, user=None, password=None):

        #set defaults on incoming argumenst
        if(uri==None):
            uri="bolt://localhost"
        
        if(user==None):
            user="neo4j"
        
        if(password==None):
            password="password"

        self._driver = GraphDatabase.driver(uri, auth=(user, password))


    def close(self):
        self._driver.close()


    def get_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            return(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

# simple code to run / test class from command line

db = HelloWorldExample()
print(db.get_greeting("message"))
