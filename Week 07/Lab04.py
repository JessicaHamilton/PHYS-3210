# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:42:44 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


#Define all variables and initial guesses
W1 = 1
W2 = 20
L1 = 3
L2 = 4
L3 = 4
L = 8
sth1 = 0.500
sth2 = 0.2588
sth3 = 0.707
cth1 = 0.8660
cth2 = 0.9659
cth3 = 0.7971
T1 = 2
T2 = 5
T3 = 7 


#define functions and calculate initial function values
y1 = L1*cth1 + L2*cth2 + L3*cth3
y2 = L1*sth1 + L2*sth2 + L3*sth3
y3 = sth1**2 + cth1**2
y4 = sth2**2 + cth2**2
y5 = sth3**2 + cth3**2
y6 = T1*sth1 - T2*sth2 - W1
y7 = T1*cth1 - T2*cth2
y8 = T2*sth2 + T3*sth3 - W2
y9 = T2*cth2 + T3*cth3

f_vector = np.array([[y1],[y2],[y3],[y4],[y5],[y6],[y7],[y8],[y9]])
#print(f_vector)
#find the partials for the functions per y
yy1 = 0 + 0 + 0 + L1 + L2 + L3 + 0 + 0 + 0 
yy2 = L1 + L2 + L3 + 0 + 0 + 0 + 0 + 0 + 0
yy3 = 2*sth1 + 0 + 0 + 2*cth1 + 0 + 0 + 0 + 0
yy4 = 0 + 2*sth2 + 0 + 0 + 2*cth2 + 0 + 0 + 0 + 0
yy5 = 0 + 0 + 2*sth3 + 0 + 0 + 2*cth3 + 0 + 0 + 0
yy6 = T1 - T2 + 0 + 0 + 0 + 0 + 0 + sth1 - sth2
yy7 = 0 + 0 + 0 + T1 - T2 + 0 + cth1 - cth2 + 0
yy8 = 0 + T2 + T3 + 0 + 0 + 0 + sth2 + sth3 + 0
yy9 = 0 + 0 + 0 + 0 + T2 - T3 + 0 + cth2 - cth3

jac = np.array([[yy1],[yy2],[yy3],[yy4],[yy5],[yy6],[yy7],[yy8],[yy9]])
#print(jac)
inv_jac = 1 / jac
#print(inv_jac)

#Start iteration for determining values
for n in range(20):
    #calculate dx
    dx = np.negative(inv_jac)*f_vector
    #update guesses with dx
    sth1 = sth1 + dx[0]
    sth2 = sth2 + dx[1]
    sth3 = sth3 + dx[2]
    cth1 = cth1 + dx[3]
    cth2 = cth2 + dx[4]
    cth3 = cth3 + dx[5]
    T1 = T1 + dx[6]
    T2 = T2 + dx[7]
    T3 = T3 + dx[8]
    #update function values 
    y1 = L1*cth1 + L2*cth2 + L3*cth3
    y2 = L1*sth1 + L2*sth2 + L3*sth3
    y3 = sth1**2 + cth1**2
    y4 = sth2**2 + cth2**2
    y5 = sth3**2 + cth3**2
    y6 = T1*sth1 - T2*sth2 - W1
    y7 = T1*cth1 - T2*cth2
    y8 = T2*sth2 + T3*sth3 - W2
    y9 = T2*cth2 + T3*cth3
    #redefine f_vector
    f_vector = np.array([[y1],[y2],[y3],[y4],[y5],[y6],[y7],[y8],[y9]])
    nummm = 10e-6
    nummm = np.int(nummm)
    if dx.any(nummm):
        break
    
    #set condition to exit for loop
    #for d in range(0, len(dx)):
        #if d <= 10e-6:
            #break
#print(T1,T2,T3,sth1,sth2,sth3,cth1,cth2,cth3)
th1 = np.arctan(sth1/cth1)
th2 = np.arctan(sth2/cth2)
th3 = np.arctan(sth3/cth3)
th11 = th1*(180/np.pi)
th22 = th2*(180/np.pi)
th33 = th3*(180/np.pi)
print("These are the respective angles:", th11,th22, th33)
print("These are the tension values:",T1,T2,T3)

#Looking at the values for the tensions and the angles, they do seems reasonable with the
#given initial guesses. The tensions are positive, the angles with respect to the x-axis,
#seem reasonable. A sketch will be included for the write up. Looking at the sketch, it
#seems reasonable for values. 

#When Using values that are either 1 or 0 for the tensions or angles will break things and make
#unrealistic. But the values that are around what I initially guess from looking at the given example
#and actually computing values of rasonable angles, it seems to stay reasonable. Extreme values do not to well.
#Larger tension values tend to predict tension values that are negative. 

#Now to test for a variety of values to find dependancy, and plot them.....step 6
def mat_funct(sth1,sth2,sth3,cth1,cth2,cth3,T1,T2,T3):
    #Define all variables and initial guesses
    W1 = 1
    W2 = 20
    L1 = 3
    L2 = 4
    L3 = 4
    L = 8 
    
    #define functions and calculate initial function values
    y1 = L1*cth1 + L2*cth2 + L3*cth3
    y2 = L1*sth1 + L2*sth2 + L3*sth3
    y3 = sth1**2 + cth1**2
    y4 = sth2**2 + cth2**2
    y5 = sth3**2 + cth3**2
    y6 = T1*sth1 - T2*sth2 - W1
    y7 = T1*cth1 - T2*cth2
    y8 = T2*sth2 + T3*sth3 - W2
    y9 = T2*cth2 + T3*cth3
    
    f_vector = np.array([[y1],[y2],[y3],[y4],[y5],[y6],[y7],[y8],[y9]])
    #print(f_vector)
    #find the partials for the functions per y
    yy1 = 0 + 0 + 0 + L1 + L2 + L3 + 0 + 0 + 0 
    yy2 = L1 + L2 + L3 + 0 + 0 + 0 + 0 + 0 + 0
    yy3 = 2*sth1 + 0 + 0 + 2*cth1 + 0 + 0 + 0 + 0
    yy4 = 0 + 2*sth2 + 0 + 0 + 2*cth2 + 0 + 0 + 0 + 0
    yy5 = 0 + 0 + 2*sth3 + 0 + 0 + 2*cth3 + 0 + 0 + 0
    yy6 = T1 - T2 + 0 + 0 + 0 + 0 + 0 + sth1 - sth2
    yy7 = 0 + 0 + 0 + T1 - T2 + 0 + cth1 - cth2 + 0
    yy8 = 0 + T2 + T3 + 0 + 0 + 0 + sth2 + sth3 + 0
    yy9 = 0 + 0 + 0 + 0 + T2 - T3 + 0 + cth2 - cth3
    
    jac = np.array([[yy1],[yy2],[yy3],[yy4],[yy5],[yy6],[yy7],[yy8],[yy9]])
    #print(jac)
    inv_jac = 1 / jac
    #print(inv_jac)
    
    #Start iteration for determining values
    for n in range(20):
        #calculate dx
        dx = np.negative(inv_jac)*f_vector
        #update guesses with dx
        sth1 = sth1 + dx[0]
        sth2 = sth2 + dx[1]
        sth3 = sth3 + dx[2]
        cth1 = cth1 + dx[3]
        cth2 = cth2 + dx[4]
        cth3 = cth3 + dx[5]
        T1 = T1 + dx[6]
        T2 = T2 + dx[7]
        T3 = T3 + dx[8]
        #update function values 
        y1 = L1*cth1 + L2*cth2 + L3*cth3
        y2 = L1*sth1 + L2*sth2 + L3*sth3
        y3 = sth1**2 + cth1**2
        y4 = sth2**2 + cth2**2
        y5 = sth3**2 + cth3**2
        y6 = T1*sth1 - T2*sth2 - W1
        y7 = T1*cth1 - T2*cth2
        y8 = T2*sth2 + T3*sth3 - W2
        y9 = T2*cth2 + T3*cth3
        #redefine f_vector
        f_vector = np.array([[y1],[y2],[y3],[y4],[y5],[y6],[y7],[y8],[y9]])
        nummm = 10e-6
        nummm = np.int(nummm)
        if dx.any(nummm):
            break
    
    th1 = np.arctan(sth1/cth1)
    th2 = np.arctan(sth2/cth2)
    th3 = np.arctan(sth3/cth3)
    th11 = th1*(180/np.pi)
    th22 = th2*(180/np.pi)
    th33 = th3*(180/np.pi)
    return th11,th22,th33, T1,T2,T3

#First to vary the tensions keeping the angles constant
angle = []
T1_array = []
T2_array = []
T3_array = []
T1 = 2
T2 = 2
T3 = 2
for a in range(20):
    test = mat_funct(0.500,0.2588,0.707,0.8660,0.9659,0.7971, T1,T2,T3)
    angle.append(test[0])
    angle.append(test[1])
    angle.append(test[2])
    T1_array.append(test[3])
    T2_array.append(test[4])
    T3_array.append(test[5])
    T1 = T1 + 0.25
    T2 = T2 + 0.25
    T3 = T3 + 0.25
    #print("These are the respective angles:", test[0], test[1], test[3])
    #print("These are the tension values:", test[0],test[2],test[3])
W1_array = np.ones(20)
a=np.empty(n); a.fill(5)
W2_array= np.empty(20); W2_array.fill(20)
plt.scatter(W1_array, T1_array, s=3, color = 'blue')
plt.scatter(W1_array, T2_array, s=3, color = 'purple')
plt.scatter(W1_array, T3_array, s=3, color = 'green')
plt.title("Testing the dependancy of Tensions versus Weight 1")
plt.xlabel('Weight1')
plt.ylabel('Tensions')
plt.show()
plt.scatter(W2_array, T1_array, s=3, color = 'blue')
plt.scatter(W2_array, T2_array, s=3, color = 'purple')
plt.scatter(W2_array, T3_array, s=3, color = 'green')
plt.title("Testing the dependancy of Tensions versus Weight 2")
plt.xlabel('Weight2')
plt.ylabel('Tensions')
plt.show()

#Now to vary the angles keeping the tensions constant
angle1 = []
angle2 = []
angle3 = []
sth1 = 0.500
sth2 = 0.2500
sth3 = 0.707
cth1 = 0.8660
cth2 = 0.9659
cth3 = 0.7971
for b in range(20):
    test1 = mat_funct(sth1,sth2,sth3,cth1,cth2,cth3,2,5,5)
    angle1.append(test1[0])
    angle2.append(test1[1])
    angle3.append(test1[2])
    sth1 = sth1 + 0.2
    sth2 = sth1 + 0.2
    sth3 = sth3 + 0.2
    cth1 = cth1 + 0.2
    cth2 = cth2 + 0.2
    cth3 = cth3 + 0.2

plt.scatter(W1_array, angle1, s=3, color= 'blue')
plt.scatter(W1_array, angle2, s=3, color = 'purple')
plt.scatter(W1_array, angle3, s=3, color = 'green')
plt.title("Testing the dependancy of Angles versus Weight 1")
plt.xlabel('Weight1')
plt.ylabel('Angles')
plt.show()
plt.scatter(W2_array, angle1, s=3, color = 'blue')
plt.scatter(W2_array, angle2, s=3, color = 'purple')
plt.scatter(W2_array, angle3, s=3, color = 'green')
plt.title("Testing the dependacny of Angles versus Weight 2")
plt.xlabel('Weight2')
plt.ylabel('Angles')
plt.show()

#In looking at the graphs produced when varying the tensions, There is a dependancy on the second tension
#and even the first tension, but not as pronounced. They do not vary much in the values. There is a uniform 
#variation of the third tension.
 
#In looking at the graphs produced for the varying angles, seems to affect the overall values more. The first 
#angle seems to cluster within a certain range, but as it reaches over -20, then it spread if larger and the 
#values are not as reasonable. The same argument is made for the third angle, but the opposite direction. As
#the values decrease in negativity, they seem seem to each a point where the variation is greater and the values
#are not as reasonable. There is not as much flexibility in the second angle, which makes sense due to it
#being determined really by the other angles. The range is smaller and once of that range, the values go
#straight to unreasonable.