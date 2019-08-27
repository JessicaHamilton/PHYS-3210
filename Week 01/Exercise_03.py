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
negligible amount to the final summation, say 1 part in 10**8.

Before writing any lines of code, discuss an approach with your neighbor 
and write out on paper how your code should proceed. Code up your approach 
in Spyder once you're done. 

Here are your tasks:

   1. Perform a Maclaurin series expansion of the function sin(x) to 
      derive the equation in the README. 
   2. Derive a generalized, finite summation form for the series based 
      on your Maclaurin series expansion.
   3. Discuss with your neighbor about how to approach coding the problem
      and write out on paper how you code should proceed. 
   4. Code your approach in Spyder once you are finished.
   5. Show that, for small values of x, the series converges.
   6. Which value for N was required to reach the desired precision and
      obtain convergence?
   7. Compare your results to the value determined using NumPy's sine 
      function.
   8. Steadily increase x and write down the relative error between your
      calculated value for sin(x) and the NumPy function's value. 
   9. What do you notice about the relative error?
  10. Will there be a time when the series does not converge? Make a plot
      of the relative error vs x to support your answer.

Created on Tue Aug 20 11:02:00 2019

@author: gafeiden
"""

import numpy as np
import matplotlib.pyplot as plt


x_values = np.arange(0,10,0.1)
def my_fact(n):
    return 1 if (n==1 or n==0) else n*my_fact(n-1)
actual_array = []
approx_array = []
err_array = []
#Create loop to access each x-value to approx.
for numm in x_values:
    #1. Print exact value
    actual = np.sin(numm)
    print('X value',numm)
    print('Actual sin(x) value:', actual)
    
    #Run approx for each x value
    summation = 0
    for each_value in range(50):
        #2. Calculate the factorial for n
        n = (2*each_value)+1
        factorial = my_fact(n)
        #3.calculate interations
        iteration = ((-1**each_value)*(numm**n))/factorial
        #4.Iteration update
        summation = summation + iteration
        if (iteration/summation) <= 1e-8:
            break
    error = abs(abs(actual) - abs(summation))/numm
    actual_array.append(actual)
    approx_array.append(summation)
    err_array.append(error)
    print('Approx value:', summation)
    print('Number of iterations:', each_value)
    print("Error:", error)
#print(actual_array, approx_array)

plt.scatter(x_values, actual_array, s=2)
plt.title('X values versus Actual sinx values')
plt.show()
plt.scatter(x_values, approx_array, s=2)
plt.title('X values versus Approx sinx values')
plt.show()
plt.plot(x_values,err_array)
plt.title('X values versus Relative Error')
plt.show()
plt.plot(actual_array, approx_array)
plt.title('Actual array versus Approx Array')
plt.show()
            
        
        
            
    

