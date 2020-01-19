package movies.spring.data.neo4j.controller;

import java.util.Map;

import movies.spring.data.neo4j.services.MovieService;

import org.slf4j.Logger;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import org.slf4j.LoggerFactory;

/**
 * @author Mark Angrish
 * @author Michael J. Simons
 */
@RestController
@RequestMapping("/")
public class MovieController {

	private final static Logger log = LoggerFactory.getLogger(MovieController.class);

	private final MovieService movieService;

	public MovieController(MovieService movieService) {
		this.movieService = movieService;
	}

	@GetMapping("/graph")
	public Map<String, Object> graph(@RequestParam(value = "limit", required = false) Integer limit) {
		return movieService.graph(limit == null ? 100 : limit);
	}

	@GetMapping("create")
	public Integer create(@RequestParam(value = "title", required = false) String title) {
		log.info("create:" + title);

		// return movieService.findByTitle(title);
		return 1;
	}

}
