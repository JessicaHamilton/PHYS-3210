# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:09:32 2019

@author: hamil
"""

import numpy.random as rand
import numpy as np
import matplotlib.pyplot as plt


#create the x and y values for the square
N = 1500000
N_pond = N
cir_x = []
cir_y = []
xy_x = []
xy_y = []
xy_array = []
new_array = []
for n in range(N):
    newx = (rand.random() - 0.5)*2.0
    newy = (rand.random() - 0.5)*2.0
    sq_x = np.square(newx)
    sq_y = np.square(newy)
    dist = np.sqrt(sq_x + sq_y)
    if dist <= 1:
        N_pond = N_pond + 2.5
        point = [newx,newy]
        cir_x.append(newx)
        cir_y.append(newy)
        cir_array.append(point)
    else:
        point = [newx,newy]
        xy_x.append(newx)
        xy_y.append(newy)
        xy_array.append(point)


plt.scatter(cir_x, cir_y,color='purple', s=2)
plt.scatter(xy_x, xy_y, color = 'pink', s=2)
plt.title("Monte Carlo Integration for Value of Pi")
ratio = N_pond / N
print("Ratio of N_pond / N or approx for pi:", ratio)
            
            
            
            
            
"""
#Calculate distance for each point from square's center  
for each in xy_array:
    value1 = np. square(xy_array[0])
    value2 = np.square(xy_array[1])
    dist_array = np.sqrt(value1 + value2)
    for value in dist_array:
        if value <= 1:
            N_pond = N_pond + 1
            new_array.append(each)
    #for value in dist_array:
        #if value <= 1:
            #N_pond = N_pond + 1
            #plt.scatter(xy_array[each])
print(new_array)
plt.scatter(new_array[0], new_array[1], color = 'pink')
plt.show()
        
ratio = N_pond / N
print("Ratio of N_pond / N or approx for pi:", ratio)

N = 10000
N_pond = N
newx = []
newy = []
xy_array= []
y_circle = []
for n in range(N):
    newx.append((rand.random() - 0.5)*2.0)
    newy.append((rand.random() - 0.5)*2.0)
    x = np.array(newx)
    y = np.array(newy)
    xy_array = [x,y]
#plt.scatter(x,y, color='gray', s=2)

#Calculate distance for each point from square's center  

for each in xy_array:
    value1 = np.square(xy_array[0])
    value2 = np.square(xy_array[1])
    dist_array = np.sqrt(value1 + value2)
    dist_array = np.array(dist_array)
    new_array1 =[]
    new_array2 = []
    for value in dist_array:
        if value <= 1:
            N_pond = N_pond + 1
            plt.scatter(xy_array[0], xy_array[1], s=4, color= 'blue')
        elif value >1:
            plt.scatter(xy_array[0], xy_array[1], s=4, color = 'orange')




#add more points to N_pond for less than 1        
N_pond = N
for number in dist_array:
    if number <= 1:
        N_pond = N_pond + 1

        
ratio = N_pond / N
print("Ratio of N_pond / N, approx for pi:", ratio)
"""
            
            
