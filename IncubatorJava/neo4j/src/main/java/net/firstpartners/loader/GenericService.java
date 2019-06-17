package net.firstpartners.loader;

import org.neo4j.ogm.session.Session;

abstract class GenericService<T> {

    private static final int DEPTH_LIST = 0;
    private static final int DEPTH_ENTITY = 1;
    protected Session session = DbSessionFactory.getInstance().getNeo4jSession();

    Iterable<T> findAll() {
        return session.loadAll(getEntityType(), DEPTH_LIST);
    }

    T find(Long id) {
        return session.load(getEntityType(), id, DEPTH_ENTITY);
    }

    void delete(Long id) {
        session.delete(session.load(getEntityType(), id));
    }

    void createOrUpdate(T entity) {
        session.save(entity, DEPTH_ENTITY);

    }

    abstract Class<T> getEntityType();
}