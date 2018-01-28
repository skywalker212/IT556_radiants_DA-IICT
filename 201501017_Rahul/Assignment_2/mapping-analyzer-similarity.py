import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv
import time

es=Elasticsearch([{"host" : "127.0.0.1", "port" : 9200}])

mapping = {

        "settings" : {
            "analysis" : {
                "analyzer" : {
                    "new_stop" : {
                            "type" : "stop",
                            "stopwords" : [","]
                        }
                    }
                }
            },	
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
			  "index_options" : "docs",
              "analyzer" : "whitespace",
			  "similarity" : "classic"
			},
			"Artist" : {
			  "type" : "text",
			  "index_options" : "docs",
              "analyzer" : "keyword"
			},
			"Genre" : {
			  "type" : "text",
			  "index_options" : "docs",
              "analyzer" : "simple"
			},
			"Subgenre" : {
			  "type" : "text",
			  "index_options" : "docs",
              "analyzer" : "new_stop"
			}
		}
	}
  }
}


es.indices.create(index = 'songs', body = mapping)

with open('albumlist.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='songs', doc_type='album')