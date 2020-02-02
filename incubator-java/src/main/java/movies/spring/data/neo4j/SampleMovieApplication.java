package movies.spring.data.neo4j;

import java.util.ArrayList;
//import java.util.Arrays;
import java.util.Iterator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.data.neo4j.repository.config.EnableNeo4jRepositories;

import movies.spring.data.neo4j.domain.Movie;
import movies.spring.data.neo4j.services.MovieService;

/**
 * @author Michael Hunger
 * @author Mark Angrish
 */
@SpringBootApplication
@EnableNeo4jRepositories("movies.spring.data.neo4j.repositories")
public class SampleMovieApplication {

    private final static Logger log = LoggerFactory.getLogger(SampleMovieApplication.class);

    public static void main(String[] args) {

        ConfigurableApplicationContext ctx = SpringApplication.run(SampleMovieApplication.class, args);
        log.info("after setup");

        // List beans
        // String[] beanNames = ctx.getBeanDefinitionNames();

        // Arrays.sort(beanNames);
        // for (String beanName : beanNames) {
        // log.info(beanName);
        // }

        // try to invoke
        try {

            MovieService myService = ctx.getBean("movieService", MovieService.class);
            log.info("got movie service bean");

            ArrayList<Movie> movies = new ArrayList<Movie>(myService.findByTitleLike("*"));
            log.info("number of movies:" + movies.size());

            Iterator<Movie> i = movies.iterator();
            while (i.hasNext()) {
                log.info("move:", i.next().getTitle());
            }

        } catch (Exception e) {
            log.error("msg", e);
        } finally {
            // force close - make more like command line app - remove to re-enable web app
            ctx.close();
        }

    }
}