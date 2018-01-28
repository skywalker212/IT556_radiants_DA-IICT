import json
from elasticsearch import Elasticsearch

es=Elasticsearch()

q1 = {
	"query" : {
		"bool" : {
			"should" : [
			{
				"match" : {
					"Artist" : "The Beatles"
				}
			},
			{
				"match" : {
					"Album" : "Revolver"
				}
			}
			],
			"minimum_should_match" : 2
		}
	}
}

print(json.dumps(es.search(index = "songs", doc_type = "album", body = q1), indent = 2))	