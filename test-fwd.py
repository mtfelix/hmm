import hmm_forward
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

T = 3
O = Table([0,1,0]) # red , white, red

print "The prob is:\n", hmm_forward.forward(A,B,pi,O)