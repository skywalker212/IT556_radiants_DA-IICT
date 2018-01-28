import json
from elasticsearch import Elasticsearch

es=Elasticsearch()

q1 = {
	"query" : {
		"bool" : {
			"must" : [
				{
					"range" : {
						"Year" : {
							"gte" : 1965,
							"lte" : 1975
						}
					}
				},
				{
					"match" : {
						"Artist" : "The Beatles"
					}
				}
			]
		}
	}
}

q2 = {
	"query" : {
		"bool" : {
			"should" : [
				{
					"range" : {
						"Year" : {
							"gte" : 1995,
							"lte" : 1998,
						}
					}
				},
				{
					"match" : {
						"Artist" : {
							"query" : "U2",
							"boost" : 2
							}
					}
				}
			]
		}
	}
}

q3 = {
	"query" : {
		"boosting" : {
			"positive" : {
				"term" : {
					"Artist" : "U2"
				}
			},
			"negative" : {
				"range" : {
					"Year" : {
						"lt" : 1990
					}
				}
			},
			"negative_boost" : 0.2
		}
	}
}

q4 = {
	"query" : {
		"bool" : {
			"filter" : {
				"term" : {
					"Artist" : "U2"
				}
			}
		}
	}
}

q5 = {
	"query" : {
		"bool" : {
			"must_not" : {
				"range" : {
					"Year" : {
						"lt" : 2000
					}
				}
			}
		}
	}
}

print(json.dumps(es.search(index = "songs", doc_type = "album", body = q1), indent = 2))
#Albums in 1965-1975 by The Beatles
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q2), indent = 2))	
#list albums released in 1990-1998 and more emphasis on albums by U2 in that time range
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q3), indent = 2))	
#More emphasis on post 1990 albums by U2
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q4), indent = 2))	
#List all albums by U2
print(json.dumps(es.search(index = "songs", doc_type = "album", body = q5), indent = 2))	
#21st century albums