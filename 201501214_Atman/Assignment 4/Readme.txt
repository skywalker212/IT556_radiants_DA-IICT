Course IT562 - Recommendation Engine And applications.
Course Instructor - Prof. Sourish Dasgupta

Assignment 4
	Tasks:
		Create a simulated data about user preference and items (music or books). Use a normalisation function to squash the preference value between 0 and 1. Make the user number to be 1 million and the songs 5 million. Use both Scikit-Learn SVD method and GenSim. Make a benchmark in terms of speed and memory utilisation.

	Performance Analysis:
		Data size 50000 X 10000 (matrix)
		Singular value decomposition using 'sklearn' for this data is done in 3.83247113228 seconds while using 'gensim' the same is done in 0.14587020874 seconds.
		This shows that gensim is much faster than sklearn (Almost 25 times faster). 