# def first_block(l):

#     max_sum = 0
#     sum_local = 0
#     first_index = 0
#     local_first_index=0
#     last_index = 0
#     for i in range(len(l)):
        
#         sum_local += l[i]

#         if sum_local < 0:
#             local_first_index = i+1
#             sum_local = 0

#         elif sum_local > max_sum:
#             first_index = local_first_index
#             last_index = i
#             max_sum = sum_local
            

#     return max_sum, first_index, last_index

# l = [8826, 8352, -1419, -2030, -9881, 7493, -4793, -4368, 9090, -51, -6917, 9155, -364, -3996, 6756, 1982, 5767, 2794, -6526, 5562]
# print(first_block(l))

# sumaa = 0
# for i in range(0, 5):
#     sumaa+=l[i]

# print(sumaa)

import pdb

pdb.set_trace()
def sum_list(L):

    sum_ = 0

    for i in L:
        sum_+=i

    return sum_

def increament_head_new(L, H, x):

    if( len(L) == 0):
        return []
    
    if(len(L) == 1):
        return [L[0]]

    s = sum_list(H)

    if(x < 0 and s < 0):
        H = [x]

    if(x<0 and s>0):
        H = [x] + H

    if(x>0 and s<0):
        H =[x]
    
    if(x>0 and s>0):
        H = [x] + H

    return H


Z = [-10, 1, 2, -100]
Y = Z.copy()
Y.reverse()


L = []
H = []

for i in range(len(Y)):

    H = increament_head_new(L, H, Y[i])
    L.insert(0, Y[i])

print(H)