"""
We are given a list of elements, with positive and negative values.
Let us first generate such a list
After generating such a list, we find out if there is a block of elements
from L[i]...L[j] such that the sum of all elements L[i]+L[i+1]+..+L[j] is the
maximum across all possible i and j.
"""
#Note that sorting doesn't help :-)

import random
def populate_list(n):
    """This function will populate the list L with n random numbers in the
    range of -1000 to +1000"""
    L=random.choices(range(-1000,1000),k=n)
    return L

def sum_total(L,i,j):
    """simply the sum of L[i]+L[i+1]+...+L[j-1]+L[j]"""
    total=0
    for k in range(i,j+1):
        total=total+L[k]
    return total


def find_max(L):
    """This will find the required i,j block which sums to the max"""
    #The idea is to select all possible i,j blocks. Simple!
    max_total=0
    max_pair=(0,0)
    for i in range(len(L)):
        for j in range(i,len(L)):
            #find the sum of the i,j block, using a separate function
            total=sum_total(L,i,j)
            if total>max_total:
                max_total=total
                max_pair=(i,j)
    return max_total,max_pair

L=populate_list(10000)
print(L)
print("**********")
max_total,max_pair=find_max(L)
print(max_total,max_pair,"Block size: ",abs(max_pair[0]-max_pair[1]))

