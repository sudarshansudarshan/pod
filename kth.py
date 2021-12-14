import random
L=list(range(20))
random.shuffle(L)
#print(L)


def kth(k,L):
    """This function finds the kth element in the list L. Assuming that 
    S is a sorted version of L, we will simply find what is S[k]. Please note,
    we dont find S and then output S[k], the challenge here is to find S[k],
    without computing the whole of S. In other words, do not sort the given
    list, but find the kth element in the sorted version of the list"""

    #Let us first create the left wing and the right wing by picking an element
    #called the pivot element. Let us consider the first element to be the
    #pivot element.
    left=[]
    right=[]
    pivot=L[0] #first element is your reference element 
    for i in range(1,len(L)):#go through everything
        if L[i]<pivot: #means it is on the left 
            left.append(L[i]) #append it on the left 
        else: #if it is on the right
            right.append(L[i]) #append it on right 
    #note that if the elments are same as pivot, they come on the right. 

    #We have created the left and right wing so far.

    #Let us be careful and try to find where our k is:

    if len(left)>k: #this means that the kth is on the left
        return kth(k,left)
    if len(left)==k: 
        return pivot 
    if len(left)<k:# a little complicated, just observe
        return kth(k-(len(left)+1) ,right)
