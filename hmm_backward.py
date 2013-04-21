''' The simple implementation of backward algorithm for HMM. 
  Just for fun and practice of Python, more considerations should be done for real use.
  
  Note: Matrix parts are borrowed from Raymond Hettinger, refer to 
   http://users.rcn.com/python/download/python.htm
  
  Coder: Hongfei Jiang @ 2013.4.21 '''
from matfunc import Table, Vec, Matrix

def backward(AMatrix,BMatrix,PiVec,Obers):
	''' The backward algorithm to calculate the probability of a oberservation sequence (Obers) 
	given lambda: AMatrix, BMatrix,PiVec '''
	prob = 0.0
	beta = []
	T = len(Obers)
	
	#step1: initialize
	for i in range (AMatrix.rows):
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