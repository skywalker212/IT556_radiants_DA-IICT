import json
from elasticsearch import Elasticsearch

es=Elasticsearch()

q1 = {
        "query" : {
			"match" : {
				"Album" : "Greatest"
			}
        }
    }

print(json.dumps(es.search(index = "songs", doc_type = "album", body = q1), indent = 2))	



 
