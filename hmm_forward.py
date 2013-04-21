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
	
	prob = 0.0 # the prob wanted
	alpha = [] # alpha is a 2-D array
	
	#step1: initialize
	for i in range (AMatrix.rows):
		alpha.append([])
	for j in range (AMatrix.rows):
		alpha[0].append(PiVec[j]*BMatrix[j][0])
		
	#step2: recursively compute alpha[t+1][i]
	for t in range (0,len(Obers)-1): #
		for i in range (AMatrix.rows):
			alpha[t+1].append(0) # create alpha[t+1][i], set default value 0
			
			for j in range (AMatrix.rows):
				#print "t,i, j is ",t,i, j, "\n"
				alpha[t+1][i] += alpha[t][j] * AMatrix[j][i]
			alpha[t+1][i] *= BMatrix[i][Obers[t+1]]
	
	#step3: sum
	T = len(Obers);
	for i in range (AMatrix.rows):
		prob += alpha[T-1][i]
		
	return prob

