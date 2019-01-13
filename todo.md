
## TODO

Next: Cosine similarity based on 



Next: Visualize topics (google how to)
    https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/

Next: visualize docs per topic (as per article below)


To try
- Gensim (and tutorial). Good for similarity queries based on common topics
https://radimrehurek.com/gensim/tut1.html (and 2)
    - use LSI for topics
    - flask to web app (dash for graphs on flask)
        (a) enter terms
        (b) inspect topics
        (c) find documents most similar to ..

Aim - get the Corpus / Vectorisation "good enough" for a pass over the CES


##Analysis
- similarity of documents
- topics per document
- try grouping (extract topics)
- try grouping (given topics)
- try closeness
- New document, find similar
- Extract possible topics
    - Extract Sales and Marketing Element
    - Extract Market
    - Extract possible ids
    - Extract possible company name
    - Extract possible issues
    - Extract end sectors
    - Extract per sector
    - sentiment analysis https://medium.com/@pmin91/aspect-based-opinion-mining-nlp-with-python-a53eb4752800
    - Sentiment analysis
    - build tagging for later machine learning


## Tidy
- Tidy off this todo.md
- update docs - put at the top of each script

Review Smart.xlsx
    - Document how to update
	- see if format useful for what trying to report now
	- move to an end user guide (what is this data showing, once reports generated)


## Medium Term
- update words in word_knowledge.xlsx 
    - rerun smart_corpus.py, check doc
    - PYTHON TESTS
    - take output newwords and add
    - filter 2 letter words in file (then tell code to ignore)
    - Better stemming
- list of countries
- better stopwords

- changes to output
    - check that we are operating on keywords
    - double keyword output
    - filter obvious words? (only show instersting, remove if then etc)
    - implement mapping (or make note to do so later)
    - implement highlight (filter into pivor table)
    - make project GDPR compliant ( delete document folder, link to repository instead)

- click for better command line handling:     http://click.pocoo.org/5/
- Github as project backup (1st step - exclude EI specifics)
- add requirements.txt (with needed libs)
    
## Web and tests
    - build on index.py to give web interface to reports
    - build on /tests - http://flask.pocoo.org/docs/0.12/testing/

## More data
Python:scrape and Analyze company directory: https://irishadvantage.com/company-directory/

## Learning actions
    - work through jupyter notebook from Colubmai
    - read articles Pocket

Positive / negative sentiment analysis
Naive Bayes classifcation of documents?

To look at: TextBlob?
To look at: NLTK book samples

Q: What way to gather my feedback (e.g. keywords, constrain to pillars / 6 elements, Markets)


Report - using 
    https://de.dariah.eu/tatom/topic_model_visualization.html#topic-model-visualization or similar
    - On above
        ○ + Date
        ○ +company year
        ○ by Salles and marketing severity
        ○ Sales and Marketing element
        by target market
        by 

