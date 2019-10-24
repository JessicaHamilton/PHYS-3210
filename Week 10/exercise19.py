# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:29:01 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def func(x_int, v_int, h,P):
    k = 0.5
    m = 1
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10,0.0001)
    for t in time:
        #update values
        vnew = vnew + (-k*h*(xnew**(P-1)))/m
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time

trialv, trialx, trialt = func(2,0.25,0.0001,2)
plt.plot(trialx,trialt)
plt.show()
plt.plot(trialt,trialx)
plt.show()

#This is what I expected when P is equal to 2. This should give the oscillating wave we expect. Since we can model
#oscillations as sinewaves. 




#varying P
P = np.arange(2,12,2)
t1, t11, time1 = func(2,0.5, 0.0001, 4)
t2, t22, time2 = func(2,0.5, 0.0001, 6)
t3, t33, time3 = func(2,0.5, 0.0001, 8)
t4, t44, time4 = func(2,0.5, 0.0001, 10)
t5, t55, time5 = func(2,0.5, 0.0001, 12)

plt.plot(t1, time1)
plt.plot(t2, time2)
plt.show()

plt.plot(t1, time1)
plt.plot(t2, time2)
plt.plot(t3, time3)
plt.plot(t4, time4)
plt.show()

plt.plot(t1, time1)
plt.plot(t2, time2)
plt.plot(t3, time3)
plt.plot(t4, time4)
plt.plot(t5, time5)
plt.show()


#To check the function varies no matter how much non-linear the equation gets.

P_array = np.arange(2,12,2)
for point in P_array:
    testv, testx, time = func(0,0.05,0.0001,point)
    plt.plot(testx, time)
    plt.title('Motion of Oscillator, varying power with initial position and initial small velocity')
plt.show()

P_array = np.arange(2,12,2)
for point in P_array:
    testv, testx, time = func(0,0.5,0.0001,point)
    plt.plot(testx, time)
    plt.title('Motion of Oscillator, varying power with initial position and initial velocity')

#When varying the power, the functions still oscillate. The shape of the functions change as you change the
#constants, specifically the initial position and the velocity.

#For the motion of the particle, it will reach max velocity when it passes through the equilibrium position (x=0)
#This is what I would expect when looking at the slope of the position function. The greatest slope is at
#that point. When you view the change in power graph, this shows a change in amplitude in correlation with the 
#change in period. If you increase the period, the amplitude will decrease. The two are inversely proportional, 
#which makes sense. 

