from surprise import SVD
import numpy as np
import surprise  # run 'pip install scikit-surprise' to install surprise
from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
import time
from guppy import hpy

reader = Reader(line_format='user item rating timestamp', sep='\t')
algo = surprise.KNNBasic()
print "-----------------------------------------------------"
print "Datasize = 10 Thousand Tuples"
data = Dataset.load_from_file('Sample_10k.data', reader=reader)
data.split(2)  # split data for 2-folds cross validation
start_time = time.time()
surprise.evaluate(algo, data, measures=['RMSE'])
print("time taken for execution: {} seconds".format(time.time()-start_time))
h = hpy()
print h.heap()
print "-----------------------------------------------------"

print "-----------------------------------------------------"
print "Datasize = 100 Thousand Tuples"
data = Dataset.load_from_file('Sample_100k.data', reader=reader)
data.split(2)  # split data for 2-folds cross validation
start_time = time.time()
surprise.evaluate(algo, data, measures=['RMSE'])
print("time taken for execution: {} seconds".format(time.time()-start_time))
h = hpy()
print h.heap()
print "-----------------------------------------------------"

print "-----------------------------------------------------"
print "Datasize = 1 Million Tuples"
data = Dataset.load_from_file('Sample_1m.data', reader=reader)
data.split(2)  # split data for 2-folds cross validation
start_time = time.time()
surprise.evaluate(algo, data, measures=['RMSE'])
print("time taken for execution: {} seconds".format(time.time()-start_time))
h = hpy()
print h.heap()
print "-----------------------------------------------------"
