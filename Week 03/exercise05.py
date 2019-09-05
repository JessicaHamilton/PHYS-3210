# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:03:35 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt



def up_harmonic(value_n):
    H_up = 0.0
    summ_array1 = []
    new_x = value_n + 1
    x_array1 = np.arange(1,new_x)
    for each_value in x_array1:
        numm1 = 1/each_value
        H_up = H_up + numm1
        summ_array1.append(H_up)
    return H_up, summ_array1
#test = up_harmonic(20)
#up_sum = test[0]
#up_values = test[1]
#print("Sum up value is:", test[0]) 
#print("The Up values are:", up_values)



def down_harmonic(value_n):
    H_down = 0.0
    summ_array2 = []
    new_x = value_n + 1
    x_array = np.arange(1,new_x)
    x_array2 = x_array[::-1]
    for each_value in x_array2:
        numm2 = 1/each_value
        H_down = H_down + numm2
        summ_array2.append(H_down)
    return H_down, summ_array2

#test1 = down_harmonic(20)
#down_sum = test1[0]
#down_values = test1[1]
#print("Sum down value is:", test1[0])
#print("The down values are:", down_values)




fraction_array = []
x_values = np.arange(1,50)
for new_value in x_values:
    test1 = up_harmonic(new_value)
    test2 = down_harmonic(new_value)
    up_sum = test1[0]
    down_sum = test2[0]
    up_array = test1[1]
    down_array = test2[1]
    print("The up sum is:", up_sum)
    print("The down sum is:", down_sum)
    sub = up_sum - down_sum
    abs_add = np.abs(up_sum) + np.abs(down_sum)
    fraction = sub / abs_add
    fraction_array.append(fraction)
    
plt.plot(x_values,fraction_array)

# When looking at the values for the sum up versus sum down, the sum down is more precise due to the fact that
#the larger the number decimal place-wise, the less values the computer can store, it will reach built in limit 
#that computer can store values. Therefore when adding smaller and smaller value numbers to already larger
#decimal placed numbers,the computer will just drop them and will not change the value. But With the sum down
#approach, you start with the small numbers and then slowly add more and more larger valued numbers. 