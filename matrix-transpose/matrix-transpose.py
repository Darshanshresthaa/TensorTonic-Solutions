import numpy as np

def matrix_transpose(A):
    if not A or not A[0]:
        return []
    transpose = []

    for i in range(len(A[0])): 
        row = []
        for j in range(len(A)):
            row.append(A[j][i])

        transpose.append(row)


    return np.array(transpose)  #we have to convert becaure out case expect the Array answer but without it array we are sending List
            
        
