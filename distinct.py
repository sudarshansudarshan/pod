def check_distinct_obvious(L):
    """
    A function that returns if the list L has distinct elements or not. 
    Will output a boolean value"""
    flag=1
    #use two for loops to look into all possible pairs.
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            #in case you see two elements being the same, declare non-distinct
            if (L[i]==L[j]):
                flag=0
    return flag

def create_movie_theatre(n):
    """
    simply creates a theatre with 100 slots
    """
    H=[]
    for i in range(n):
        H.append([])
    return H

def put_element(x,H):
    """x is a person with a aadhar number and we look at the
    last 2 digits and put that person in H[last two digits]"""
    H[x%len(H)].append(x)
    return H

def put_list(L,H):
    for x in L:
        H=put_element(x,H)
    return H

def present_or_not(x,V):
    """x is an element, V is a list, we will just check linearly
    if x is present in V or not"""
    flag=0
    for i in range(len(V)):
        if x==V[i]:
            flag=1
    return flag

#main motive is to come out with a genius method for check_distinct.
def check_distinct_genius(L):
    """The central idea is the following:
    We take every single element and push that to its respective seat in the
    theatre, as we push, we check, if the same element is present in the
    vertical or not"""
    #creat a movie theatre
    H=create_movie_theatre(len(L))

    #for every person, put him to his respective seat and check that vertical
    #if his number is present already or not.
    flag=1
    for i in range(len(L)):
        seat_number=L[i]%len(L)
        if present_or_not(L[i],H[seat_number]):
            flag=0
        H[seat_number].append(L[i])
    return flag












