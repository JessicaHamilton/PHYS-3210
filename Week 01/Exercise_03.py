# -*- coding: utf-8 -*-
"""
Exercise 03: Chapter 03, Kinder & Nelson

A common way to determine the value of a function is to sum over a series. 
For example, the Maclaurin series for sin(x) is

    sin(x) = x - x**3/3! + x**5/5! - x**7/7! + ...

Perform a series expansion to derive the equation above. Next, write down 
a general expression for the sum of the series that is valid between n = 0 
and n = N, where N ≥ 0. This will serve as your algorithm for summing 
the series.

One problem with the algorithm is that we do not know which value 
of N is suitable when calcualting the series. Instead of guessing, have 
your code proceed with the summation until the Nth term contributes a 
negligible amount to the final summation, say 1 part in 10**8. We call 
this _numerical convergence_.

Before writing any lines of code, discuss an approach with your neighbor 
and write out on paper how your code should proceed. Code up your approach 
in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(_x_) to 
      derive the equation above. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of _x_, the algorithm converges and that
      it converges to the correct value by comparing your results to the
      value determined using NumPy's sine function.
   6. Which value for _N_ was required to reach the desired precision
      to obtain numerical convergence for small values of _x_?
   7. Steadily increase _x_ and write down the relative error between your
      calculated value for sin(_x_) and the NumPy function's value. 
   8. What do you notice about the relative error?
   9. Will there be a time when the series does not numerically converge? 
      Make a figure or two from the data you generate to support your 
      conclusion.
  10. _Challenge_ How can you modify your algorithm to be valid for any
      value of _x_?

Created on Tue Aug 20 11:02:00 2019

@author: gafeiden
"""


import numpy as np
import matplotlib.pyplot as plt


x_values = np.arange(0.001,30,0.1)
def my_fact(n):
    return 1 if (n==1 or n==0) else n*my_fact(n-1)
actual_array = []
approx_array = []
err_array = []
summation = 0
#Create loop to access each x-value to approx.
for numm in x_values:
    #1. Calculate actual value
    actual_value = np.sin(numm)    
    print('X value:',numm)
    print('Actual sin(x) value:', actual_value)
    
    #Run approx for each x value
    for each_value in range(50):
        #2. Calculate the factorial for n
        a = (2*each_value)+1
        factorial = my_fact(a)
        #3.calculate interations
        iteration = (((-1)**each_value)*(numm**a))/factorial
        #4.Iteration update
        summation = summation + iteration
        if abs(iteration/summation) <= 1e-8:
            break
    error = np.abs(actual_value - summation)/numm
    actual_array.append(actual_value)
    approx_array.append(summation)
    err_array.append(error)
    print('Approx value:', summation)
    print('Number of iterations:', each_value)
    print("Error:", error)

plt.scatter(x_values, actual_array, s=2)
plt.title('X values versus Actual sinx values')
plt.show()
plt.scatter(x_values, approx_array, s=2)
plt.title('X values versus Approx sinx values')
plt.show()
plt.scatter(x_values,err_array, s=2)
plt.title('X values versus Relative Error')
plt.show()

            
# Trying to add in the Phase folding.....        
x_values = np.arange(0.001,30,0.1)
def my_fact(n):
    return 1 if (n==1 or n==0) else n*my_fact(n-1)
actual_array = []
approx_array = []
err_array = []
#Create loop to access each x-value to approx.
for numm in x_values:
    #1. Calculate actual value
    actual_value = np.sin(numm)
    new_x = 0
    #Phase folding
    if np.sign(numm) == 1:
        m = numm//2*np.pi
        new_x = numm-(2*np.pi*m)
        actual_value = np.sin(new_x)
    elif np.sign(numm) == -1:
        m = numm//2*np.pi
        new_x = numm+(2*np.pi*m)
        actual_value = np.sin(new_x)
    print(new_x)    
    print('X value:',numm)
    print('Actual sin(x) value:', actual_value)
    
    #Run approx for each x value
    summation = 0.0
    for each_value in range(50):
        #2. Calculate the factorial for n
        a = (2*each_value)+1
        factorial = my_fact(a)
        #3.calculate interations
        iteration = (((-1)**each_value)*(new_x**a))/factorial
        #4.Iteration update
        summation = summation + iteration
        if abs(iteration/summation) <= 1e-8:
            print(abs(iteration/summation))
            break
    error = np.abs(actual_value - summation)/numm
    actual_array.append(actual_value)
    approx_array.append(summation)
    err_array.append(error)
    print('Approx value:', summation)
    print('Number of iterations:', each_value)
    print("Error:", error)


plt.scatter(x_values, actual_array, s=2)
plt.title('X values versus Actual sinx values')
plt.show()
plt.scatter(x_values, approx_array, s=2)
plt.title('X values versus Approx sinx values')
plt.show()
plt.scatter(x_values,err_array, s=2)
plt.title('X values versus Relative Error')
plt.show()        
            
    


