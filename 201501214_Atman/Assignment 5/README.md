# Estimating SVD through Stochastic Gradient Descent  
--------------------------------------------------------------------
Calcutate RMSE, Runtime and Memory used for a given dataset and compare for different datasets  
The data is in the form User, Item, Rating, Timestamp.

## Approach  
--------------------------------------------------------------------
For this task there are many libraries available for Python. Here the library 'surprise' is used, which has many inbuilt algorithms for SVD and we can analyze our custom algorithm as well. This library also allows us to use sample large dataset availabe as well as the custom dataset.

Here I have analyzed 3 different algorithms.

  - MatrixFacto (Custom Algorithm) Link: http://nbviewer.jupyter.org/github/NicolasHug/nicolashug.github.io/blob/master/assets/mf_post/Matrix%20factorization%20algorithm.ipynb
  - SVD (Inbuilt Algorithm)
  - KNNBasic (Inbuilt Algorithm)

To check all the algorithms 3 different size of custom dataset has been used.
  - Dataset with 10 thousand tuples.
  - Dataset with 100 thousand tuples.
  - Dataset with 1 million tuples.
--------------------------------------------------------------------
## Output
### Using MatrixFacto()
Data Size (Number Of Tuples) | RMSE (Root Mean Square Error) | Run Time (Seconds) | Memory Utilization (Bytes)
--- | --- | --- | --- 
10,000 | 2.2954 | 0.9952 | 21,341,240
100,000 | 0.9877 | 10.5243 | 51,035,488
1,000,000 | 0.9211 | 117.7920 | 361,714,296
-------------------------------------------------------------------

### Using SVD()
Data Size (Number Of Tuples) | RMSE (Root Mean Square Error) | Run Time (Seconds) | Memory Utilization (Bytes)
--- | --- | --- | --- 
10,000 | 1.0290 | 0.6629 | 21,334,032
100,000 | 0.9567 | 7.0232 | 51,031,000
1,000,000 | 0.9027 | 86.0800 | 361,705,552
-------------------------------------------------------------------

### Using KNNBasic()
Data Size (Number Of Tuples) | RMSE (Root Mean Square Error) | Run Time (Seconds) | Memory Utilization (Bytes)
--- | --- | --- | --- 
10,000 | 1.1983 | 0.2250 | 21,341,312
100,000 | 1.0044 | 13.8129 | 51,035,392
1,000,000 | 0.9428 | 561.9454 | 361,714,544

## Graphs for MatrixFacto() Algorithm
--------------------------------------------------------------------

### RMSE
![rmse-graph](https://github.com/skywalker212/IT556_radiants_DA-IICT/blob/master/201501214_Atman/Assignment%205/RMSE_Graph.PNG)

### Runtime
![runtime-graph](https://github.com/skywalker212/IT556_radiants_DA-IICT/blob/master/201501214_Atman/Assignment%205/Run_Time_Graph.PNG)

### Memory  
![memory-graph](https://github.com/skywalker212/IT556_radiants_DA-IICT/blob/master/201501214_Atman/Assignment%205/Memory_Graph.PNG)

--------------------------------------------------------------------

As we can see for any algorithm to estimate SVD:

    - RMSE decreases with increase in data count
    - Runtime increases with increase in data count
    - Memory Usage increases with increase in data count
