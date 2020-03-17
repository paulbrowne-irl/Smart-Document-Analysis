// delete all nodes
MATCH (n)
DETACH DELETE n

// delete all testdata
MATCH (N{testdata:true}) 
DETACH DELETE N