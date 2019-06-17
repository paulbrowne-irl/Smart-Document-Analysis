package net.firstpartners.loader;

import org.neo4j.ogm.config.Configuration;
import org.neo4j.ogm.session.SessionFactory;
import org.neo4j.ogm.session.Session;

public class DbSessionFactory {

    private final static Configuration configuration = new Configuration.Builder().uri("bolt://localhost:11002")
            .credentials("neo4j", "password").build();
    private final static SessionFactory sessionFactory = new SessionFactory(configuration, "school.domain");
    private static DbSessionFactory factory = new DbSessionFactory();

    public static DbSessionFactory getInstance() {
        return factory;
    }

    // prevent external instantiation
    private DbSessionFactory() {
    }

    public Session getNeo4jSession() {
        return sessionFactory.openSession();
    }
}