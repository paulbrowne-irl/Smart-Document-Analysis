## Next

+ Cosine similarity - make sure script and todo is documented
+ smart_analyse_gensim_topics.py  make sure script and todo is documented, promote back from incubators
+ Better visualations on existing scripts

## Housekeeping
+ Update docs - put at the top of each script
+ Review Smart.xlsx
    - Document how to update
	- see if format useful for what trying to report now
+ Upgrade readme.md to an end user guide (what is this data showing, once reports generated)
+ Build on index.py to give web interface to reports
+ Build on /tests - http://flask.pocoo.org/docs/0.12/testing/


## Play and decide next step
+ Investigate Apache Superset (for visualisations)
+ Investigate Scattertext for visualisation
+ Visualize topics (google how to) https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/
+ Inspect using Python Feature tools (google how to use for NLP)
+ Gensim (and tutorial). Good for similarity queries based on common topics https://radimrehurek.com/gensim/tut1.html (and 2) use LSI for topics
+ Sentiment Analysis: https://medium.com/@pmin91/aspect-based-opinion-mining-nlp-with-python-a53eb4752800



## Target Analysis Aims
+ Aim - get the Corpus / Vectorisation "good enough" for a pass over the CES
+ Similarity of documents
+ topics per document
+ try grouping (extract topics)
+ try grouping (given topics)
+ try closeness
+ New document, find similar
+ Extract possible topics
    - Extract Sales and Marketing Element
    - Extract Market
    - Extract possible ids
    - Extract possible company name
    - Extract possible issues
    - Extract end sectors
    - Extract per sector
    - sentiment analysis 
    - build tagging for later machine learning
    - Key issues

## Data Sources
* Saved Reports
* Company reports ## More data
Python:scrape and Analyze company directory: https://irishadvantage.com/company-directory/
* Search online for Business Corpus


## Medium Term
- update words in word_knowledge.xlsx 
- rerun smart_corpus.py, check doc
- Python Tests
 take output newwords and add
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



## Learning actions / Bucket
+ Work through jupyter notebook from Colubmai
+ read articles Pocket
+ Positive / negative sentiment analysis
+ Naive Bayes classifcation of documents?
+ To look at: TextBlob?
+ To look at: NLTK book samples

Q: What way to gather my feedback (e.g. keywords, constrain to pillars / 6 elements, Markets)


## Reporting - using 
+ https://de.dariah.eu/tatom/topic_model_visualization.html#topic-model-visualization or similar
    + Date
    + Company year
    + by Salles and marketing severity
    + Sales and Marketing element
    + by target market
      
