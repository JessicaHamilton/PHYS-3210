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

#Work through exercise 5.1
time = np.linspace(0,10,101)
A = 240000
B = 900
alpha = 1
beta = 1000

viral_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)
#plot 
plt.scatter(time,viral_load, s=2, color= 'green', label= 'Model')
plt.title("Concentration of Viral Load Versus Time")
plt.xlabel("Time")
plt.ylabel("Concentration")


#load data and assign variables
HIV_data = np.load(r"\Users\hamil\Documents\Github\PHYS-3210\Week 01\data\HIVseries.npz")
data_time = HIV_data['time_in_days']
data_viralload = HIV_data['viral_load']
plt.scatter(data_time, data_viralload, color = 'navy', label= 'Actual')
plt.legend()
plt.show()




#Create function for fitting the data

def fitting(A,B,alpha,beta,time):
    import numpy as np
    import matplotlib.pyplot as plt
    #define equation
    v_load = A*np.exp(-alpha*time)+B*np.exp(-beta*time)
    return v_load

#Testing out the function by varying alpha and A while beta and B are fixed
#plot all and save to a pdf

HIV_data = np.load(r"\Users\hamil\Documents\Github\PHYS-3210\Week 01\data\HIVseries.npz")
data_time = HIV_data['time_in_days']
data_viralload = HIV_data['viral_load']
second = plt.scatter(data_time, data_viralload, color = 'navy', label= 'Actual')
plt.title("Concentration of Viral Load Versus Time")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()

time = np.linspace(0,10,101)
test1 = fitting(240000,900,1,1000,time)
test2 = fitting(2000,900,5,1000,time)
test3 = fitting(10000,900,4,1000,time)
test4 = fitting(50000,900,3,1000,time)
test5 = fitting(100000,900,2,1000,time)
test6 = fitting(240000,900,0.80,1000,time)

plt.scatter(time,test2,s=2, Label='Test1')
plt.scatter(time,test3,s=2, label='Test2')
plt.scatter(time,test4,s=2, label='Test3')
plt.scatter(time,test5,s=2, label='Test4')
plt.scatter(time,test1,s=2, label='Test5')
plt.scatter(time,test6, s=2, label= 'Test6')
plt.title("Concentration of Viral Load Versus Time")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.legend()
plt.savefig("TestingViralLoad.pdf")








    