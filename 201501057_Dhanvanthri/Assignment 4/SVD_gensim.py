#SVD of 50000 X 10000 Matrix using gensim
#Importing all the libraries
from sklearn.random_projection import sparse_random_matrix
import numpy as np
import timeit
from sklearn.preprocessing import normalize
import sys
import gensim

users = 10000
songs = 50000
print("Generating Data of 10000 users and 50000 songs")
X = sparse_random_matrix(songs,users, density=0.01, random_state=45)
#Normalizing Data between 0 and 1
X = np.absolute(X)
X_Norm = normalize(X, norm='l1', axis=0)

print "Input Data"
print (X_Norm)
print "Performing SVD..."
start = timeit.default_timer()
mat= gensim.models.lsimodel.stochastic_svd(X,6,50000)
stop = timeit.default_timer()

print "singular values"
print mat[1]
print "Left singular values"
print mat[0]
print "Time taken to perform SVD:"
print stop-start," Seconds"
