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
