# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:29:18 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as lin
import scipy.linalg as sclin

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

#part b
B = [[52,17,2], [-32,30, 19], [-9,-8,30]]
np.array(B)
c= B/det
print("Part B to check in equal in values:", c)


#Exercise 2 to find values of x in correlation to values in different values of B vector
b1 = np.array([12,-25,32])
b2 = np.array([4,-10,22])
b3 = np.array([20,-30,40])

#Solving for x1
x1 = lin.solve(A, b1)
print("This is the solution for the x-values with B1:", x1)
x2 = lin.solve(A, b2)
print("This is the solution for the x-values with B2:", x2)
x3 = lin.solve(A, b3)
print("This is the solution for the x-values with B3:", x3)


#Exercise 3
#use eigenproblem solver to determine if the eigenvalues and eigenvectors are complex conjugates
D = [[8,2], [-2,8]]
dd, ddd = lin.eig(D)
print("Value of eigenvalues:", dd)
print("Values of eigenvectors:", ddd)

#exercise 4
#determine the eigenvalues and vectors for a matrix and verify 
Mat = [[-2,2,-3], [2,1,-6], [-1,-2,0]]
mm, mmm = lin.eig(Mat)
print("Eigenvalues for Mat Matrix:", mm)
print("Eigenvectors for Mat Matrix:", mmm)

#check if eigenvalue for 5 is proprot to the following
x1 = np.array([-1,-2,1])
eigg = x1*(1/np.sqrt(6))
print("Verify they match:", eigg)

#check how the are related, the linearly indep ones and the depent one
x2 = np.array([-2,1,0])
eigg2 = x2*(1/np.sqrt(5))
x3 = np.array([3,0,1])
eigg3 = x3*(1/np.sqrt(10))
print(eigg2, eigg3)
print(eigg, eigg2, eigg3)

#I am not sure how there eigenvectors and the eigen value -3 are related. 


#Exercise 5
matr = sclin.hilbert(100)
print(matr)












