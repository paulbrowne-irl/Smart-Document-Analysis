package net.firstpartners.loader;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;

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

		DocumentService dbService = new DocumentService();
		dbService.findAll();

		// Document myDoc = new Document();
		// myDoc.name = "some name";
		// myDoc.fileName = "c:\\downloads\\something.txt";
		// myDoc.fullText = "bibba bibba bibba bibba";

	}

	public static void main(String[] args) {
		logger.info("running main");

		SpringApplication app = new SpringApplication(Neo4Japplication.class);
		app.setWebApplicationType(WebApplicationType.NONE);
		app.run(args);

	}

}
