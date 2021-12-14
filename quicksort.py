def quicksort(L):
    if (len(L)==0):
       return L 
    if (len(L)==1):
       return L
    Ram=[]
    Lakshman=[]
    Pivot=L[0]  
    for i in range(1,len(L)):
        if L[i]<Pivot:
            Ram.append(L[i])
        else:
            Lakshman.append(L[i])
    #At this point, I know the Pivot element, I have created
    #a list for Ram and another list for Laxman. Hoping that
    #I can trust them, I will outsource this work to them and return
    #the list, assuming that they will sort their respective lists.
    return quicksort(Ram)+[Pivot]+quicksort(Lakshman)

