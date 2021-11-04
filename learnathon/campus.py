import random

#below is the most important function. Once this is done. Rest is a cake walk.

def simple_transfer(x,X,Y):
    """Will simply remove x in X and put that to Y"""
    X=X.remove(x)
    Y=Y.append(x)

def transfer(x,X,Y,p):
    """put the element x in X to Y with probability p.
    Note that you should remove x in X after you include that in Y"""
    #generate a random number r between 0 to 1.
    #this will help us simulate a coin toss.
    if x in X:
        r=random.random()
        #if this random number is less than p, it is heads and is tail otherwise 
        if r<p:
            #now we need to put x into Y and remove it in X.
            X.remove(x)
            Y.append(x)
    else:
        print("Exception error, you cannot remove a non-existing element")


def main_experiment():

    Hostel=list(range(1000))
    Mess=[]
    Library=[]
    CHostel=Hostel.copy()
    CMess=Mess.copy()
    CLibrary=Library.copy()
    for i in range(10):
        for x in CHostel:
            r=random.random():
            if r<.4:
                simple_transfer(x,Hostel,Mess)
            if r>=.4 and r<.5:
                simple_transfer(x,Hostel,Library)
        for x in CMess:
            r=random.random()
            if r<.5:
                simple_transfer(x,Mess,Hostel)
            if r>=.5 and r<.9:
                simple_transfer(x,Mess,Library)
        for x in CLibrary:
            r=random.random()
            if r<.1:
                simple_transfer(x,Library,Mess)
            if r>=.1 and r<.7:
                simple_transfer(x,Library,Hostel)
        CHostel=Hostel.copy()
        CMess=Mess.copy()
        CLibrary=Library.copy()
        print(len(CHostel),len(CMess),len(CLibrary))
