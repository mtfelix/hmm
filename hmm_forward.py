''' The simple implementation of forward algorithm for HMM. 
  Tested using the example 10.2 in Pg 177 of Li Hang's Book: (Statistical Learning Methods).
  Just for fun and practice of Python, more considerations should be done for real use.
  
  Note: Matrix parts are borrowed from Raymond Hettinger, refer to 
   http://users.rcn.com/python/download/python.htm
  
  Coder: Hongfei Jiang @ 2013.4.21 '''
from matfunc import Table, Vec, Matrix


def forward(AMatrix, BMatrix, PiVec, Obers):
	''' The foward algorithm to calculate the probability of a oberservation sequence (Obers) 
	given lambda: AMatrix, BMatrix,PiVec '''
	
	# verification for the dimensions of input matrix and vector
	# # A is NxN, B is NxV, Pi is N, O is T
	# # N is the number of state classes,
	# # V is the number of obervation classes
	# # T is an arbitrary integer(>0)
	assert AMatrix.rows == AMatrix.rows 
	assert AMatrix.rows == BMatrix.rows
	assert AMatrix.rows == len(PiVec)
	
	# !!! Note that the oberservation ID is used as the index for BMatrix's second dimension (col),
	# thus, the oberservation numbers should be integers in (0 <= i < BMatrix.cols)
	assert BMatrix.cols == len(set(Obers)) # check V
	
	
	prob = 0.0 # the prob wanted
	alpha = [] # alpha is a 2-D array
	T = len(Obers)
	
	#step1: initialize
	for i in range (T):
		alpha.append([])
	for j in range (AMatrix.rows):
		alpha[0].append(PiVec[j]*BMatrix[j][0])
		
	#step2: recursively compute alpha[t+1][i]
	for t in range (T-1): #
		for i in range (AMatrix.rows):
			#print "t,i:",t,i
			alpha[t+1].append(0) # create alpha[t+1][i], set default value 0
			
			for j in range (AMatrix.rows):
				alpha[t+1][i] += alpha[t][j] * AMatrix[j][i]
			alpha[t+1][i] *= BMatrix[i][Obers[t+1]]
	
	#step3: sum
	T = len(Obers);
	for i in range (AMatrix.rows):
		prob += alpha[T-1][i]
		
	return prob

