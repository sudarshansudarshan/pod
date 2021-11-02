import pdb
import time
import math
import random


def populate(n):
    """
    Populate the list L and return it. Populate it with
    n elements sampled from the range (start,end)

    Parameters
    ----------
    n : elements in the list
    start : starting range of the random function to sample.
    end : end range of the random function to sample.
    
    Returns
    -------
    A list with n elements.

    """
    #use a for loop to pick n elements in the range of
    #start to end.
    L=[]
    for i in range(n):
        #using a built in random function.
        L.append(int( (random.random())*(10**16)))
    return L

def create_table(L,delta):
    """
    Given the list L create a hash table and return the same.
    Use the parameter delta to create the hash table. delta
    is the difference between the closest two elements.
    """    
    #create an empty list of empty lists, this will be
    #our hash table with n elements, where n is the length
    #of the given list. 
    H=[]
    for i in range(len(L)):
        H.append([])
        
    #after creating an empty hash table, include all the
    #elements of L into the hash table
    
    #for every point x in L
    for x in L:
        #find out which delta house it is in and
        #put x into its appropriate delta house
        #which is simply int(x/delta)
        H[(int(x/delta))%len(H)].append(x)
    return H

def sort_first_few(L,k):
    """
    This will sort the first k elements in the list and returns back the list
    Takes L and returns L where the first k elements of L is sorted. 
    """
    #works only if L has more than 100 elements
    if len(L)>k: 
       #then sort the list using the obvious sorting technique 
       for i in range(k):
           mini=i
           for j in range(i+1,k):
               if L[j]<L[mini]:
                   mini=j
           L[i],L[mini]=L[mini],L[i]
    return L


def disturbance(H,Points,new_point,delta):
    """
    Parameters
    ----------
    H: The hashtable
    Points : All the points
    new_point : The new point that is added
    delta : The delta in Points

    Returns
    -------
    0: if the new point creates disturbance
    1: if the new point doesn't create any disturbance
    also returns the point that is creating the disturbance
    along with the new_point

    """
    #We need to check if the newly added point creates
    #any disturbance.
    #distance is when its delta house has another point
    #or its 1st or 2nd neighbor has a point whose distance
    #from the new_point is less than delta. 
    #We just return 0 or 1
    delta_address=int(new_point/delta)
    neighbors=[]
    neighbors.extend(H[(delta_address-2)%len(H)])
    neighbors.extend(H[(delta_address-1)%len(H)])
    neighbors.extend(H[(delta_address-0)%len(H)])
    neighbors.extend(H[(delta_address+1)%len(H)])
    neighbors.extend(H[(delta_address+2)%len(H)])
    
    disturbing_point=math.inf
    new_delta=delta
    flag=0
    for x in neighbors:
        if (abs(x-new_point)<new_delta):
            new_delta=abs(x-new_point)
            disturbing_point=x
            flag=1
    return flag,disturbing_point

def push_hash(H,new_point,delta):
    """
    Simply pushes the new_point to the hashtable H.

    Parameters
    ----------
    H : The Hashtable
    new_point : The new point that needs to be pushed to
    the hash table
    delta : the existing closest pair distance. Note 
    that this doesn't change or get updated. This is
    only used to hash the new_point.

    Returns
    -------
    the hash table H.

    """
    delta_address=int(new_point/delta)
    H[delta_address%len(H)].append(new_point) 
    return H


def iteratively_add_number(H,Points,new_point,delta,a,b):
    """
    This will add a number to the existing list of numbers
    and check if this results in a disturbance. If it does
    result in a disturbance, it will rehash the points
    using a new delta value.
    
    Returns Hashtable, updated points, new delta

    Returns
    -------
    Hashtable(updated), Points(update), delta(updated), (a,b)
    where a,b are the points

    """
    
    #we assume that the list 'Points' has atleast 3 points.

    #flag will contain if there is disturbance or not. 
    #disturbing_point will be that number which will pair up with the new_point
    #which is creating the disturbance, thus contributing to the new delta
    #which is delta=abs(new_point-disturbing_point)
    flag,disturbing_point=disturbance(H,Points,new_point,delta)

    if new_point==disturbing_point:
        return H,Points,0,new_point,disturbing_point


    #in case the new point creates disturbance
    if (flag==1):
        #we know that the delta is disturbed, we compute the new delta
        delta=(abs(disturbing_point-new_point)/2)
        #We append the new point to the list.
        Points.append(new_point)  
        #redo the hashtable using the new delta value
        H=create_table(Points,delta)
        a=new_point
        b=disturbing_point


    #else, if it doesn't create any disturbance
    else:
        #update the Points list with the new point
        Points.append(new_point)
        #update the hashtable H with the new point.
        H=push_hash(H,new_point,delta)

    return H,Points,delta,a,b        

def closest_pair_obvious(L):
    a=L[0]
    b=L[1]
    mini=abs(L[1]-L[0])
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if abs(L[i]-L[j]) <mini:
                a=L[i]
                b=L[j]
                mini=abs(a-b)
    return a,b,mini

def closest_pair_obvious1(L):
    X=L.copy()
    X.sort()
    a=X[0]
    b=X[1]
    delta=abs(a-b)
    for i in range(2,len(X)):
        new_delta=abs(X[i]-X[i-1])
        if new_delta<delta:
            a=X[i-1]
            b=X[i]
            delta=new_delta
    return a,b,delta


def closest_pair_genius(L):
    #simply sort the first 100 elements in the list L.
    #and for the rest, iterate through it. 
    a,b,delta=closest_pair_obvious(L[0:100])
    if (delta==0):
        return a,b,delta
    else:
        H=create_table(L[0:100],delta)
    Points=L[0:100]
    for i in range(100,len(L)):
        H,Points,delta,a,b=iteratively_add_number(H,Points,L[i],delta,a,b)
        if (delta==0):
            return a,b,delta
    return a,b,abs(b-a)

n=10000000
L=populate(n)

t1=time.time()
print(t1)
print(closest_pair_genius(L))
t2=time.time()
print(t2-t1)



