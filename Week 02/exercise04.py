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
A = 3
B = 0
alpha = 12
beta = 20

viral_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)

plt.scatter(time,viral_load, s=2)
plt.title("Viral Load versus Time")


#Now for dataset
#load data and assign variables
HIV_data = np.loadtxt(r"\Users\hamil\Documents\Github\PHYS-3210\Week 01\data\HIVseries.csv")
print(HIV_data)
data_time = HIV_data[0]
print(data_time)
data_viralload = HIV_data[1]
print(viralload)
plt.plot(data_time, data_viralload)







#def viral_load(A,B,alpha,beta,time):
   # return viral_load = A* np.exp(-alpha*time)+B* np.exp(-beta*time)