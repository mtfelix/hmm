''' The simple implementation of viterbi algorithm for HMM. 
  Just for fun and practice of Python, more considerations should be done for real use.
  
  Note: Matrix parts are borrowed from Raymond Hettinger, refer to 
   http://users.rcn.com/python/download/python.htm
  
  Coder: Hongfei Jiang @ 2013.4.21 '''
from matfunc import Table, Vec, Matrix


def viterbi(AMatrix, BMatrix, PiVec, Obers):
	''' The viterbi algorithm to predict the most likely state sequence  
	given lambda: AMatrix, BMatrix,PiVec and the oberservation sequence (Obers)'''
	
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
	
	
	best_state_seq = [] # the best state sequence wanted
	delta = [] # delta is a 2-D array
	psi = [] # psi is a 2-D array
	T = len(Obers)
	
	#step1: initialize
	for i in range (T):
		delta.append([])
		psi.append([])
	for i in range (AMatrix.rows):
		delta[0].append(PiVec[i] * BMatrix[i][Obers[0]])
		psi[0].append(-1) # state is 0-indexed, thus -1 stands for null state
		
	#step2: recursively compute delta[t][i] and psi[t][i]
	for t in range(1,T):
		for i in range(AMatrix.rows):
			#print "t,i:",t,i
			best_prob = delta[t-1][0] * AMatrix[0][i] # default state: 0
			best_pre_state = 0
	
			for j in range (AMatrix.rows):
				if best_prob < ( delta[t-1][j] * AMatrix[j][i] ) :
					best_prob = delta[t-1][j] * AMatrix[j][i]
					best_pre_state = j
			
			best_prob *= BMatrix[i][Obers[t]]
			#print "t,i:", t,i,len(delta[t]);
			delta[t].append(best_prob)
			psi[t].append(best_pre_state)
			
	#step3: terminate
	best_p = delta[T-1][0]
	last_best_state = 0
	for i in range(AMatrix.rows):
		if best_p < delta[T-1][i]:
			best_p = delta[T-1][i]
			last_best_state = i
	
	#step4: backtrack the best state sequence
	
	best_state_seq.append(last_best_state)
	#print last_best_state
	next_best_state = last_best_state
	for t in reversed(range(T-1)):
		cur_best_state = psi[t+1][next_best_state]
		best_state_seq.append(cur_best_state)
		#print cur_best_state
		next_best_state = cur_best_state
	
	best_state_seq.reverse()
	return  best_state_seq

