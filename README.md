# Summary

Analyze a set of documents (from companies) to give a useful snapshot or summary.
Original Documents are left unmodified, the only reports modified are in the z_output folder

## Expected folder structure

Most scripts have a parameter to point to the client documents (e.g. '..').
There is also parameters to exclude folders (e.g. like the z_scripts folder itself) from the analysis

+ CLIENT DOCS
+ Client 1 Folder
\ sample word doc
\ sub folder
  \ sample xl doc
+ client 2 Folder

## Scripts

The key user scripts are in the main top level directory.
The top of each script contains parameters to modify the script behaviour

* one_client_pdf.py - gather all client data into one pdf
* snapshot.py - make a summary of client documents (e.g. last updated, size, number, sentiment etc)


## Script Struture

+ data - data objects
+ extract - extract information from file
+ info - generate info / insights
+ report - report these insights
+ templates - templates used in reporting
+ test_data - does what it says on the tin
+ z_output - output- may be deleted by scripts


===

* tmp delte

# What project is 

some blurb

# Some samples

Powerpoint
1 Type of questions
2 Comapny-document-key-conents
3 graph
4 graph db
5 the document graph
