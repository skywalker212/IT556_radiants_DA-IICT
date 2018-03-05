#SVD of 50000 X 10000 Matrix using sklearn
#Importing all the libraries
from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
import numpy as np
import timeit
from sklearn.preprocessing import normalize

users = 10000
songs = 50000
print("Generating Data of 10000 users and 50000 songs")
X = sparse_random_matrix(songs,users, density=0.01, random_state=45)
#Normalizing Data between 0 and 1
X = np.absolute(X)
X_Norm = normalize(X, norm='l1', axis=0)
svd = TruncatedSVD(n_components=6, n_iter=7, random_state=42)

print "Input Data"
print (X_Norm)
print "Performing SVD..."
start = timeit.default_timer()
svd.fit(X_Norm)
stop = timeit.default_timer()

print "Variance ratio Of all components"
print(svd.explained_variance_ratio_)  
print "Sigma - Diagonal entries"
print(svd.explained_variance_ratio_.sum())  
print(svd.singular_values_) 
print("VT Matrix")
print (svd.components_)
print "Time taken to perform SVD:"
print stop-start," Seconds"
