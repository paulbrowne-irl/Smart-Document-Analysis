package net.firstpartners.loader.data;

import org.neo4j.ogm.annotation.*;

/*
 * Represents a Text Document
 */
@NodeEntity
public class Document {

    public Document() {
    }

    public String name;
    public String fileName;
    public String fullText;

}