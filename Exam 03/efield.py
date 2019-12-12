# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:27:30 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


#define variables needed
g = 2
g_t= 0
tau = 2
omega = 0.5
h = 0.0001 

#define functions to use in euler's method
#def y_0(x):
#    return x
def y_1(t):
    return (y_2(t))
def y_2(y1new):
    return (-1*(omega**2)*y1new - (1/tau*y1new - (g-g_t*(y1new**2))))

#set up arrays needed and initialize variables
t_array = np.arange(0,10,h)
y1_array = []
y2_array = []
y2new = y_2(t_array[0])
y1new = y_1(t_array[0])



#loop over functions
for num in t_array: 
    y2new = y2new + y_2(y1new)*h
    y2_array.append(y2new)
    
    y1new = y1new + y2new*h
    y1_array.append(y1new)
    
    
plt.plot(t_array, y1_array)
plt.title('Electric field as a function of time')
plt.show()    

#now plot the two functions in phase space
plt.plot(y1_array, y2_array)
plt.title('Tejectory of System in phase space')
plt.show()    



    
# To test how the function changes with changing g_t
gtarray = np.arange(0,1.1,0.1)
for a in gtarray:
    g = 2
    g_t= a
    tau = 2
    omega = 0.5
    h = 0.0001 
    
    #define functions to use in euler's method
    #def y_0(x):
    #    return x
    def y_1(t):
        return (y_2(t))
    def y_2(y1new):
        return (-1*(omega**2)*y1new - (1/tau*y1new + (g-g_t*(y1new**2))))
    
    #set up arrays needed and initialize variables
    t_array = np.arange(0,10,h)
    y1_array = []
    y2_array = []
    y2new = y_2(t_array[0])
    y1new = y_1(t_array[0])
    
    
    #loop over functions
    for num in t_array: 
        y2new = y2new + y_2(y1new)*h
        y2_array.append(y2new)
        
        y1new = y1new + y2new*h
        y1_array.append(y1new)
        
        
    plt.plot(t_array, y1_array)
    plt.title('Electric field as a function of time')
    
plt.show()
    
for a in gtarray:
    g = 2
    g_t= a
    tau = 2
    omega = 0.5
    h = 0.0001 
    
    #define functions to use in euler's method
    #def y_0(x):
    #    return x
    def y_1(t):
        return (y_2(t))
    def y_2(y1new):
        return (-1*(omega**2)*y1new - (1/tau*y1new + (g-g_t*(y1new**2))))
    
    #set up arrays needed and initialize variables
    t_array = np.arange(0,10,h)
    y1_array = []
    y2_array = []
    y2new = y_2(t_array[0])
    y1new = y_1(t_array[0])
    
    
    #loop over functions
    for num in t_array: 
        y2new = y2new + y_2(y1new)*h
        y2_array.append(y2new)
        
        y1new = y1new + y2new*h
        y1_array.append(y1new)
        
        
    plt.plot(y1_array, y2_array)
    plt.title('Trajectory of System in phase space')
 
plt.show()    


    
    
    