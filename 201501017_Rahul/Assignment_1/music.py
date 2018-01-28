import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv
import time

es=Elasticsearch([{"host" : "127.0.0.1", "port" : 9200}])

mapping = {
	"mappings" : {
		"album" : {
		  "properties" : {
			"Number" : {
			  "type" : "long"
			},
			"Year" : {
			  "type" : "long"
			},
			"Album" : {
			  "type" : "text",
			  "index_options" : "docs"
			},
			"Artist" : {
			  "type" : "text",
			  "index_options" : "docs"
			},
			"Genre" : {
			  "type" : "text",
			  "index_options" : "docs"
			},
			"Subgenre" : {
			  "type" : "text",
			  "index_options" : "docs"
			}
		  }
		}
	}
}

q1 = {
	"query" : {
		"match" : {
			"Album" : "Revolver"
		}
	}
}

q2 = {
	"query" : {
		"range" : {
			"Year" : {
				"gte" : 2000
			}
		}
	}
}

q3 = {
	"query" : {
		"bool" : {
			"must" : [
				{
					"range" : {
						"Year" : {
							"gte" : 1965,
							"lte" : 1980
						}
					}
				},
				{
					"match" : {
						"Artist" : {
							"query" : "The Beatles",
							"operator" : "and"
						}
					}
				}
			]
		}
	}
}

q4 = {
	"query" : {
		"match" : {
			"Album" : {
				"query" : "Aevolxer",
				"fuzziness" : 2
			}
		}
	}
}


es.indices.create(index = 'songs', body = mapping)

with open('albumlist.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='songs', doc_type='album')

time.sleep(2)
	
print ("q1")
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q1), indent = 2))	#search album "Revolver"
print ("q2")
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q2), indent = 2))	#search 21st century albums
print ("q3")
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q3), indent = 2))	#search for "The Beatles" albums in 1965-1980
print ("q4")
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q4), indent = 2))	#search for album "Revolver" with 2 spelling mistakes