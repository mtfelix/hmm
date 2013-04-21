''' The simple implementation of backward algorithm for HMM. 
  Just for fun and practice of Python, more considerations should be done for real use.
  
  Note: Matrix parts are borrowed from Raymond Hettinger, refer to 
   http://users.rcn.com/python/download/python.htm
  
  Coder: Hongfei Jiang @ 2013.4.21 '''
from matfunc import Table, Vec, Matrix

def backward(AMatrix,BMatrix,PiVec,Obers):
	''' The backward algorithm to calculate the probability of a oberservation sequence (Obers) 
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
	
	prob = 0.0
	beta = []
	T = len(Obers)
	
	#step1: initialize
	for i in range (T):
		beta.append([])
	for j in range (AMatrix.rows):
		beta[T-1].append(1)
	
	#step2: recursively compute beta[t][i]
	for t in reversed(range(T-1)): # T-2, ..., 0 (0-indexed)
		for i in range (AMatrix.rows):
			beta[t].append(0) # create beta[t][i], set default value 0
			for j in range (AMatrix.rows):
				beta[t][i] += AMatrix[i][j] * BMatrix[j][Obers[t+1]] * beta[t+1][j]
			
	#step3: sum
	for i in range (AMatrix.rows):
		prob += PiVec[i] * BMatrix[i][Obers[0]] * beta[0][i]
		
	return prob