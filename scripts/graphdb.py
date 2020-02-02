from neo4j import GraphDatabase

#Sample class to interact with neo4j
class DB_Access(object):

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
if __name__ == '__main__':
    db = DB_Access()
    print(db.get_greeting("message"))
