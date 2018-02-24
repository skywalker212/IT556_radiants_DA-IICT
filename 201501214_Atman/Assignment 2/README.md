# Assignment 2
----------------------------
### 1. Analyzer
  Analyzers are the ones which decide by which rules the text will be divided from. We can use analyzers which are built in or we can create our custom analyzer.

### 2. Similarity Algorithms
  These are Algorithms which will decide how the score will be calculated and will display the results accordingly. The default similarity algorithm is BM25.

### 3. Normalizer
  The normalizer property of keyword fields is similar to analyzer. The normalizer is applied prior to indexing the keyword, as well as at search-time.

### 4. Boost
  Individual fields can be boosted automatically — count more towards the relevance score — at query time. So the boosted fields will get more weight in the score and will be more relevant.

 ---------------------------
 ### Query DSL
 We have run the python file ```mapping-analyzer-similarity.py``` to create an index first and then add the data from the albumlist.csv file which was used in the Assignment 1.

 You can execute queries with different analyzers by running ```analyzers-query.py``` file.

 You can run different boolean queries by using the ```bool-boost-boosting.py``` file.

Also you can run different should clause queries which will specify minimum numbers of should clauses that must match. You can check this by running ```min-should.py```
