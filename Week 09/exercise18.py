# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:17:06 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy 
from scipy import optimize
from scipy import stats


data = np.loadtxt('pi_meson_decays.dat')
time = data[:,0]
decay = data[:,1]
print(time)
print(decay)

plt.scatter(time, decay, s=3)
plt.title("Decay versus time")
plt.xlabel('time')
plt.ylabel('decays')
plt.show()
#Looking at the provided data table, the graph looks reasonable compared to figure 7.7 in the book.


#Now calculate the uncertainity and replot the data with the uncertainities
uncert = np.sqrt(len(decay))
decay_std = np.std(decay)
plt.errorbar(time,decay, yerr = uncert, linestyle = "None", fmt= '.', markersize = 7)
plt.xlabel('time')
plt.ylabel('decays')
plt.title("Decay versus time with uncertainities")
plt.show()



#define the function to fit the data
N = len(decay)
lamb = 1 / time
y = N*(np.exp(-lamb*time))
def func(time, N, lamb):
    return N*(np.exp(-lamb*time))  
    
sig_y = decay - uncert
curve1, curve2 = optimize.curve_fit(func, time, decay)
print(curve1, curve2)
fit_eq = np.poly1d(curve1)
print("Estimated curve fit:", fit_eq)

#Plot fit
x = np.arange(0,125,1)
newy = func(x, curve1[0], curve1[1])
plt.plot(x,newy, color= 'blue')
plt.scatter(time,decay, color = 'pink')
plt.xlabel('time')
plt.ylabel('decays')
plt.title("Decay versus time with fitted model")
plt.show()







#Now use the linear equation to estimate the curve fit
def linfunc(time, N, lamb):
    return np.log(N) - (lamb*time)


#normalize data for fitting and plot 
denom = np.sqrt(np.sum(decay**2))
norm_decay = decay / denom
plt.scatter(time,norm_decay)
plt.title('Normalize with mean')
plt.xlabel('Time')
plt.ylabel('Normalized Decays')
plt.show()

#plot with errorbars
plt.errorbar(time, norm_decay, yerr = uncert, linestyle = "None", fmt= '.', markersize = 7)
plt.xlabel('time')
plt.ylabel('decays')
plt.title("Decay versus time of linear model with uncertainities")
plt.show()

#estimate curve fit
curve3, curve4 = optimize.curve_fit(linfunc, time, norm_decay)
print(curve3, curve4)
perr = np.sqrt(curve4[1,1])
lin_eq = np.poly1d(curve3)
print('estimated linear curve fit:', lin_eq)


#plot data with estimated curve fit
x2 = np.arange(0,0.25,0.01)
liny = func(x2, curve3[0], curve3[1])
newy = np.log(liny)
plt.plot(x2, newy, color = 'blue')
plt.scatter(time, norm_decay, color = 'pink')
plt.xlabel('time')
plt.ylabel('decays')
plt.title("Decay versus time with linear fitted model")
plt.show()
#Plot with errorbars
plt.errorbar(x2,newy, yerr= uncert, linestyle = "None", fmt = '.', markersize = 7)
plt.title('Decay versus time with calculated error')
plt.xlabel('Time')
plt.ylabel('Normalized Decays')
plt.show()


#Do another curve fit option
slope, interc, r_value, p_value, std_dev = stats.linregress(time, decay)
print("Estimated Linear regression fit", slope, interc)
print('Estimated error:', std_dev)
combined = np.poly1d([slope,interc])
yyy = combined(x)

#Plot each way
plt.plot(x,yyy, color='purple')
plt.scatter(time,decay, s=10, color = 'pink')
plt.title("linear Regression Model")
plt.xlabel('Time')
plt.ylabel('Linearized Decays')
plt.show()
#with error bars
plt.errorbar(x,yyy, yerr=std_dev,linestyle = "None", fmt = '.', markersize = 4)
plt.scatter(time,decay, s=10, color = 'pink')
plt.title('Linear Regression with errorbars')
plt.xlabel('Time')
plt.ylabel('Linearized Decays')
plt.show()








