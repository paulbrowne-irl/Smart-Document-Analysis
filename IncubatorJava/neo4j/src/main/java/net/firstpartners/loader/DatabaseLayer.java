package net.firstpartners.loader;

import org.neo4j.ogm.config.Configuration;
import org.neo4j.ogm.session.SessionFactory;
import org.neo4j.ogm.session.Session;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Code for talking to the Database
 */

public class DatabaseLayer implements AutoCloseable {

	private static final Logger logger = LoggerFactory.getLogger(DatabaseLayer.class);

	// private Driver driver;
	SessionFactory sessionFactory;

	public DatabaseLayer() {
		this("bolt://localhost:11002", "neo4j", "password");
	}

	public DatabaseLayer(String uri, String user, String password) {
		// driver = GraphDatabase.driver(uri, AuthTokens.basic(user, password));
		Configuration configuration = new Configuration.Builder().uri(uri).credentials(user, password).build();

		sessionFactory = new SessionFactory(configuration, "net.firstpartners.loader.data");

	}

	@Override
	public void close() throws Exception {
		// driver.close();
		sessionFactory.close();
	}

	public void persist(Object node) {

		Session session = sessionFactory.openSession();
		session.save(node);
		sessionFactory.close();

	}
	/*
	 * public void printGreeting(final String message) throws Exception {
	 * 
	 * Session session = driver.session(); String greeting =
	 * session.writeTransaction(new TransactionWork<String>() {
	 * 
	 * @Override public String execute(Transaction tx) { StatementResult result =
	 * tx.run("CREATE (a:Greeting) " + "SET a.message = $message " +
	 * "RETURN a.message + ', from node ' + id(a)", parameters("message", message));
	 * return result.single().get(0).asString(); } });
	 * 
	 * logger.info(greeting);
	 * 
	 * }
	 */
}
