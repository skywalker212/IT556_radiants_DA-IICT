#This file contains all the mapping with analyzers, similarities and normalizers
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv
import time
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')

es=Elasticsearch([{"host" : "127.0.0.1", "port" : 9200}])

mapping = {
        "settings" : {
            "analysis" : {
                "analyzer" : {
                    "coma_separate" : {
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
              "analyzer" : "simple",
              "similarity" : "boolean"
			},
			"Subgenre" : {
			  "type" : "text",
			  "index_options" : "docs",
              "analyzer" : "coma_separate",
              "similarity" : "boolean"
			}
		}
	}
  }
}


es.indices.create(index = 'songs', body = mapping)

with open('albumlist.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='songs', doc_type='album')