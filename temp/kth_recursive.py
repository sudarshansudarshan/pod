import random
import pdb
def populate(n,i,j):
    L=[]
    for i in range(n):
        L.append(random.randint(i,j))
    return L


def kthelement(L,k):
    if len(L)==1:
        return L[0]

    leftwing=[]
    rightwing=[]
    first=L[0]
    for i in range(len(L)):
        if L[i]<first:
            leftwing.append(L[i])
        else:
            rightwing.append(L[i])
    if len(rightwing)<k:
        return kthelement(leftwing,k)
    else:
        return kthelement(rightwing,len(L)-k)

pdb.set_trace()
L=populate(20,1000,2000)
print(L)
print(kthelement(L,4))
    

