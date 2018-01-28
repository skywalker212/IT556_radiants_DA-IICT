import json
from elasticsearch import Elasticsearch

es=Elasticsearch()

q1 = {
        "query" : {
			"bool" : {
				"must" : [
				{
					"match" : {
						"Album" : "Calling"
					}
				},
				{
					"match" : {
						"Artist" : "The Clash"
					}
				}
				]
			}
        }
    }

q2 = {
        "query" : {
			"match" : {
				"Artist" : "the beatles"
			}
        }
    }
q3 = {
        "query" : {
			"match" : {
				"Artist" : "The Beatles"
			}
        }
    }
q4 = {
       "query" : {
			"match" : {
				"Subgenre" : "rock&roll"
				}
        }
    }

q5 = {
       "query" : {
			"match" : {
				"Genre" : "funk"
				}
        }
    }

	print(json.dumps(es.search(index = "songs", doc_type = "album", body = q1), indent = 2))	
# q1 : returns result because "London Calling" will be analyzed into ["London" , "Calling"] due to whitespace analyzer which will match with our query. 
#Also using must we are doing logical and between artist query and album query
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q2), indent = 2))
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q3), indent = 2))
# q2 :no result because "Artist" is analyzed as keyword and documents will be indexed with "The Beatles" and we are searching for "the beatles"
# q3 :gives some results
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q4), indent = 2))	
# q4 : gives albums with subgenre Rock&Roll. As stopwords is only "," "rock&roll" will analyzed as "Rock&Roll" and not ["rock", "roll"].
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q5), indent = 2))	
# q5 : gives albums having genre Funk. Also gives result if Genre is "Funk/Soul" because it will be analyzed into ["funk", "soul"]. "/" being non-letter 
#will be dropped


 
