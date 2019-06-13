package net.firstpartners.loader;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import net.firstpartners.loader.data.Document;

import org.springframework.boot.CommandLineRunner;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@SpringBootApplication
public class Neo4Japplication implements CommandLineRunner {

	private static final Logger logger = LoggerFactory.getLogger(Neo4Japplication.class);

	public Neo4Japplication() {

	}

	/** main run method */
	@Override
	public void run(String... args) throws Exception {
		logger.info("In run method");
		DatabaseLayer dbLayer = new DatabaseLayer();

		Document myDoc = new Document();
		myDoc.name = "some name";
		myDoc.fileName = "c:\\downloads\\something.txt";
		myDoc.fullText = "bibba bibba bibba bibba bibba bibba bibba bibba bibba bibba ";

		dbLayer.persist(myDoc);
		dbLayer.close();
	}

	public static void main(String[] args) {
		logger.info("running main");
		SpringApplication.run(Neo4Japplication.class, args);
	}

}
