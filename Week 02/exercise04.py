# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:41:01 2019

@author: hamil
"""
#Follow exercise 5.1 in book then create a function to do the same thing
#Write a function for the viral load after antiviral drug delivered. exercise5
#The input will be : A,B,alpha, beta, time. Also plot variations of A and alpha

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0,10,101)
A = 240000
B = 900
alpha = 1
beta = 1000

viral_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)

plt.scatter(time,viral_load, s=2, color= 'green', label= 'Model')
plt.title("Viral Load versus Time")


#Now for dataset
#load data and assign variables
HIV_data = np.load(r"\Users\hamil\Documents\Github\PHYS-3210\Week 01\data\HIVseries.npz")
data_time = HIV_data['time_in_days']
data_viralload = HIV_data['viral_load']
plt.scatter(data_time, data_viralload, color = 'navy', label= 'Actual')

plt.legend()




#Create function for fitting the data

def fitting(A,B,alpha,beta,time):
    #load data and assign variables
    #time must be defined outside of function at calling
    HIV_data = np.load(r"\Users\hamil\Documents\Github\PHYS-3210\Week 01\data\HIVseries.npz")
    data_time = HIV_data['time_in_days']
    data_viralload = HIV_data['viral_load']
    #define equation
    v_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)
    #plot all
    first = plt.scatter(data_time, data_viralload, color = 'navy', label= 'Actual')
    second = plt.scatter(time,v_load, s=2, color= 'green', label= 'Model')
    plt.legend()
    plt.title("Concentration of Viral Load Versus Time")
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    return first,second
    
fitting(240000,900,1,1000,time)    