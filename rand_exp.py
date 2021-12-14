import random
def rand_exp(n):
    B=[0,1]
    L=[]
    for i in range(n):
        L.append(random.choice(B))
    return L
