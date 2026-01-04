import pandas as pd
import numpy as np
from scipy.linalg import null_space

A = np.array([
    [2 , -1 , 0 , 0],
    [-1 , 2 , -1 , 0],
    [0 , -1 , 2 , -1],
    [0 , 0 , -1 , 2]
])

#connection between bank :

matrix_A_transpose = np.transpose(A)
if (A == matrix_A_transpose).all():
  print("Matrix is Symmetric \n")
else:
  print("Matrix is not Symmetric \n")
print(matrix_A_transpose)

#RANK
rank_A = np.linalg.matrix_rank(A)
print("Rank of Matrix A is :",rank_A,"\n")

#Determinant
det_A = np.linalg.det(A).round()
print("Determinant of Matrix A is : ",det_A,"\n")

#Trace
trace_A = np.trace(A)
print("Trace of A is : ",trace_A,"\n")

#Null Space
null_space_A = null_space(A)
print("Null Space of A is : \n",null_space_A,"\n")
