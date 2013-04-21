import hmm_forward
import hmm_backward
import hmm_viterbi
from matfunc import Table, Vec, Matrix

## example 10.2 from Li Hang's book (Statistical Learning Methods), pg. 177

a1 = Table([0.5,0.2,0.3])
a2 = Table([0.3,0.5,0.2])
a3 = Table([0.2,0.3,0.5])

A = Matrix([a1,a2,a3])
#print "matrix A is:\n", A

b1 = ([0.5,0.5])
b2 = ([0.4,0.6])
b3 = ([0.7,0.3])

B = Matrix([b1,b2,b3])
#print "matrix B is:\n", B

pi = Vec([0.2,0.4,0.4])

O = Table([0,1,0,1,1,1,0]) # 0:red 1:white

print "The prob computed by fwd is:\n", hmm_forward.forward(A,B,pi,O)

print "The prob computed by bwd is:\n", hmm_backward.backward(A,B,pi,O)

print "The best state sequence predicted by the given model using viterbi is:\n",hmm_viterbi.viterbi(A,B,pi,O)