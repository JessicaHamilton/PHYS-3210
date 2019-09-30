# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:29:18 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as lin

#create matrix 
A = [[4,-2,1],[3,6,-4],[2,1,8]]
A = np.array(A)
print("Initial Matrix:", A)
#compute determinate of matrix
a = A[0][0]
b = A[0][1]
c = A[0][2]
d = A[1][0]
e = A[1][1]
f = A[1][2]
g = A[2][0]
h = A[2][1]
i = A[2][2]
det_one = a*((e*i) - (f*h))
det_two = b*((d*i)-(f*g))
det_three = c*((d*h)-(e*g))
det = det_one - det_two + det_three
print("The determinant:", det)

#Transpose the matrix
A_t = np.transpose(A)
print("Transpose of A:",A_t )
A_inverse = (1/det)*A_t
print("Inverse of A:", A_inverse)


#Computing inverse with built-in function
A_inv = lin.inv(A)
print("Function calculation of Inverse:", A_inv)
