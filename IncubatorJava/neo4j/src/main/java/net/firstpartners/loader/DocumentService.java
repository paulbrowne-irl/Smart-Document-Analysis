package net.firstpartners.loader;

import net.firstpartners.loader.data.Document;

class DocumentService extends GenericService<Document> {

    @Override
    Iterable<Document> findAll() {
        return session.loadAll(Document.class, 1);
    }

    // @Override
    // Iterable<Map<String, Object>> getStudyBuddiesByPopularity() {
    // String query = "MATCH (s:StudyBuddy)<-[:BUDDY]-(p:Student) return p, count(s)
    // as buddies ORDER BY buddies DESC";
    // return DbSessionFactory.getInstance().getNeo4jSession().query(query,
    // Collections.EMPTY_MAP);
    // }

    @Override
    Class<Document> getEntityType() {
        return Document.class;
    }
}