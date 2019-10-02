# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:01:04 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

#Define a function to calculate the integral by random sampling (pond idea)
def Probint(N, initial, final, limit):
    topx = []
    topy = []
    botx = []
    boty = []
    N_out = N
    #for each iteration, randomly generate the x and y values and calculate actual x**2 value
    for n in range(N):
        x = rand.uniform(initial,final)
        y = rand.uniform(initial,limit)
        y2 = x**2
        #determine which is greater and append to correct array
        if y > y2:
            N_out = N_out - 1
            topx.append(x)
            topy.append(y)
            #top_array = [x,y]
        elif y < y2:
            botx.append(x)
            boty.append(y)
            #bot_array = [x,y2]
    #calculate the total number of points and the results
    ratio = N_out/N
    area = final*limit
    results = area*ratio
    return results, topx,topy,botx,boty


test1, topx,topy,botx,boty = Probint(1000000, 0, 10, 100)
print("The estimated value is:", test1)
plt.scatter(topx, topy, s=2, color = 'green')
plt.scatter(botx, boty, s=2, color = 'blue')
plt.title("Distrubition of values for Integral of X**2")
plt.show()

#With 100,000 iterations, my function was able to get around a reasonable answer for 
#for the integral of x**2 from 0 to 10. Even better result occurred with 1 million iterations.
#This is a reasonable value for the fact that it is
#calculated from randomly generated numbers. But it is interesting that you can use the distributation
#function to determine the integral of a function. Based on the fact that we have a correlation to 
#area.




#Now use the function to calculate the integral for sin(x)
def Probint2(N, initial, final, up_limit, down_limit):
    topx = []
    topy = []
    botx = []
    boty = []
    N_out = N
    for n in range(N):
        x = rand.uniform(initial,final)
        y = rand.uniform(initial,up_limit)
        y2 = np.sin(x)
        if (y < y2) and (y >= 0) or (y > y2) and (y <= 0):
            topx.append(x)
            topy.append(y)
            N_out = N - 2
        else:
            botx.append(x)
            boty.append(y)
    tot_top = len(topy)
    tot_bot = len(boty)
    ratio = N/N_out
    lowx = np.min(botx)
    highx = np.max(botx)
    lowy = np.min(boty)
    highy = np.max(boty)
    xvalue = highx+lowx
    yvalue = highy+lowy
    area = xvalue*yvalue
    result = area*ratio
    return result, topx,topy,botx,boty

test2, toppx, toppy, bottx, botty = Probint2(1000000, -2*np.pi, 2*np.pi, 1, -1)
print("The estimated value is:", test2)
plt.scatter(toppx, toppy, s=2, color = 'purple')
plt.scatter(bottx, botty, s=2, color = 'pink')
plt.title("Distrubition of Values for Integral of sin(x)")
plt.ylim(-1,1)
#plt.xlim(-2*np.pi, 2*np.pi)
plt.show()

#Here when looking at the calculated value from my function compared to the analytical value,
#my result is smaller by a couple orders of magnitude. It is close,but not quite there. I do not
#believe the function will be able to accurately calculate the integral of sin(x) from 0 to 10.
#With one million iterations alreasy, I do not know how feasible this method would be to precisely 
#calculate the value. It is a good estimation though. But, the variation of the results for several runs,
#create too much uncertainity. 


#Now create a new function to calculate the integral of. 

