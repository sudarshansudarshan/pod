import numpy
def iterate(a,b):
    #the given matrix M
    M=[[12,14],[15,20]]
    #convert it to matrix format, so that mult is easy
    M=numpy.mat(M)
    #The given vector (a,b), denoted by V
    V=[a,b]
    #we take its transpose, so that we can matmul
    V=(numpy.mat(V)).T
    #the actual matrix multiplation
    V=M*V
    #finding out the norm of this vector
    #so that we can divide it.
    alpha=numpy.linalg.norm(V)
    #we are dividing the vector by its norm,
    #so that we project it to unit circle.
    V=V/alpha
    return V
#a=9023978851
#b=8725825895
a=1
b=1

V=[a,b]
V=numpy.mat(V)
V=V.T
a=V[0,0]
b=V[1,0]

#iterate 10 times and see what are all the values.
for i in range(100):
    next_vector=(iterate(a,b))
    a=next_vector[0,0]
    b=next_vector[1,0]
    print(a,b)


