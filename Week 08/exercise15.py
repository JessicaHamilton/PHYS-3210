# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:13:51 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize 

#Plot the function to determine what the finction looks like to helps estimate a value
Eb = np.arange(0,10, 0.1)
y = (np.sqrt(10 - Eb)*np.tan(np.sqrt(10-Eb)) - np.sqrt(Eb))


plt.plot(Eb, y)
plt.ylim(-50,50)
plt.title("Even function with binding potential of 10")
plt.grid()
plt.show()


#Now use the Bisection method to determine where F(Eb) = 0
def funct(Eb):
    return (np.sqrt(10 - Eb)*np.tan(np.sqrt(10-Eb)) - np.sqrt(Eb))


guess = optimize.bisect(funct, 8, 9)
print("Guess for the Bisection Method:", guess)



#Now use the Newton / Raphson Method to determine where F(Eb) = 0
x0 = 8.5

newguess = optimize.newton(funct, x0)
print("Guess for the Newton/Raphson Method:", newguess)

#When looking at the two results, there are quite similar to 10**-8 decimal place.
#Then the question would be which is more accurate, both are precise to 10**-8. 

#Now we can check the values returned for each method within our function

test1 = funct(guess)
test2 = funct(newguess)
print("The f(Eb) values for the Bisection method result and the Newton/Raphson method:", test1,test2)

#Based on the values determined by the two different methods, the second method, Newton/Raphson 
#is more precise. This would be due to the fact that the result is two orders of magnitude smaller
#(closer to zero).

#Show that the equation is the alternative form for the original equation
y2 = ((np.sqrt(Eb)*(1/np.tan(np.sqrt(10-Eb))))-(np.sqrt(10-Eb)))
plt.plot(Eb,y)
plt.plot(Eb,y2)
plt.ylim(-50,50)
plt.title("Both functions with binding potential of 10")
plt.grid()
plt.show()
#This equation seems to be a mirror of the first equation. This equation also does not extend deeply
#into negative values. I believe that the root is equal or relatively close to being
#equal to the original equation.

def funct2(Eb):
    return ((np.sqrt(Eb)*(1/np.tan(np.sqrt(10-Eb))))-(np.sqrt(10-Eb)))

guess3 = optimize.bisect(funct2, 8,9)
guess4 = optimize.newton(funct2, x0)
print("Guess for the Bisection and Newton/Raphson methods for equation two:", guess3, guess4)


#Now to change the value of 10 to 20 and 30 within the functions
y3 = (np.sqrt(20 - Eb)*np.tan(np.sqrt(20-Eb)) - np.sqrt(Eb))
y4 = (np.sqrt(Eb)*(1/np.tan(np.sqrt(20-Eb))))-(np.sqrt(20-Eb))

plt.plot(Eb,y3)
plt.plot(Eb, y4)
plt.title("Functions with binding potential of 20")
plt.grid()
plt.show()


y5 = (np.sqrt(30 - Eb)*np.tan(np.sqrt(30-Eb)) - np.sqrt(Eb))
y6 = (np.sqrt(Eb)*(1/np.tan(np.sqrt(30-Eb))))-(np.sqrt(30-Eb))

plt.plot(Eb,y5)
plt.plot(Eb, y6)
plt.title("Functions with binding potential of 30")
plt.xlim(5,10)
plt.grid()
plt.show()

#When you change the binding potential to 20, is really shows how the mirror each other.
#Once you change the value to 30, the even function actually goes to zero and the other
#function significantly peaks at around 8.


#Now to find the roots for each new value
def funct3(Eb):
    return (np.sqrt(20 - Eb)*np.tan(np.sqrt(20-Eb)) - np.sqrt(Eb)) 
#redo functions then use methods to find roots to compare
def funct4(Eb):
    return (np.sqrt(30 - Eb)*np.tan(np.sqrt(30-Eb)) - np.sqrt(Eb))

x1 = 6
guess5 = optimize.bisect(funct3,5,7)
guess6 = optimize.newton(funct3, x1)
print("Guess for bisection and Newton Methods with binding potential set to 20:", guess5, guess6)

guess7 = optimize.bisect(funct4,8,15)
guess8 = optimize.newton(funct4, x0)
print("Guess for bisection and Newton Methods with binding potential set to 30:", guess5, guess6)
test3 = funct3(guess5)
test4 = funct3(guess6)
test5 = funct4(guess7)
test6 = funct4(guess8)
print("The y values for the function with binding potential of 20:", test3, test4)
print("The y values for the function with binding potential of 30:", test5, test6)


#When looking at the root values for the function with the two different binding potentials,
#it seems the binding potential at 30 is more unrealistic and the values of the root does not make
#too much sense. I would say the best binding potential would be between 10 and 20. The values for
#for the function are very close again, this time to the 10*-10. WHen looking at the values for f(Eb),
#the bisection method seems to be better for the binding potential set to 20, since it is positive.
#the function with binding potential set to 30 seems to be fairly off due to the fact that the 
#f(Eb) values are both negative for both methods. With that being said over all (All functions) the Newton/Raphson
#method seems to be more precise. 


#Now to try another method to find the roots and test the precision
#Lets use Ridder's method and compare to the others:
guesses = optimize.ridder(funct,8,9)
print("This is the guess for the Ridder Method:", guesses)
print("again the bisection and Newtons/Raphson:", guess, newguess)

#Now to check the precision of all three together
test9 = funct(guesses)
print("Respective precisions for Bisection, Newton/Raphson, Ridder:", test1,test2,test9)

#It seems the precision for the bisection and the ridder are on the same scale and the precision for the 
#Newton/Raphson is better. This makes sense with the similarities between the bisection method and the 
#ridder method. But the ridder tends to run faster than the bisection. This method uses the false position method
#a trial and error method but tends to have a better constraint on the tolarance. This method also determines that
#convergance is guarunteed such as the bisection method. 

