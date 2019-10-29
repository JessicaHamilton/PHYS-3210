# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:49:31 2019

@author: hamil
"""
import numpy as np
import matplotlib.pyplot as plt


def rkfunc(x_int, v_int, h, P):
    k = 5
    m = 1
    x_array = []
    v_array = []
    #create initial steps
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10, 0.0001)
    for t in time:
        #calculate half steps
        v_half = vnew + (-k*(h/2)*(xnew**(P-1)))/m
        x_half = xnew + vnew*(h/2)
        #update x and v values
        vnew = vnew + ((-k*(h/2)*(x_half**(P-1)))/m)
        xnew = xnew + h*(v_half)
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time


testv, testx, testt = rkfunc(1,0.5,0.0001, 4)    
plt.plot(testx, testt)
plt.title('Runga Kutta Method First Plot')
plt.show()

#to vary P we can find:

test1, test11, test111 = rkfunc(2, 0, 0.0001, 2)
test2, test22, test222 = rkfunc(2, 0, 0.0001, 4)
test3, test33, test333 = rkfunc(2, 0, 0.0001, 6)
test4, test44, test444 = rkfunc(2, 0, 0.0001, 8)
test5, test55, test555 = rkfunc(2, 0, 0.0001, 10)


plt.plot(test11, test111)
plt.plot(test22, test222)
plt.plot(test33, test333)
plt.title('Runga Kutta Method over with P=2,4,6')
plt.show()
plt.plot(test33, test333)
plt.plot(test44, test444)
plt.plot(test55, test555)
plt.title('Runga Kutta Method over with P=6,8,10')
plt.show()
"""
P = np.arange(2,12, 2)
for p in P:
    t, tt, ttt = rkfunc(2, 0, 0.0001, p)
    plt.plot(tt, ttt)

plt.show()
"""

#Now compare the two methods:

def func(x_int, v_int, h,P):
    k = 0.5
    m = 1
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10,0.0001)
    for t in time:
        #update values
        vnew = vnew + (-k*h*(xnew**(P-1)))/m
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time


testa, testaa, testaaa = rkfunc(2, 0, 0.0001, 2)
testb, testbb, testbbb = rkfunc(2, 0, 0.0001, 4)
testc, testcc, testccc = rkfunc(2, 0, 0.0001, 6)
testd, testdd, testddd = rkfunc(2, 0, 0.0001, 8)
teste, testee, testeee = rkfunc(2, 0, 0.0001, 10)

plt.subplot(121)
plt.plot(test11, test111)
plt.plot(test22, test222)
#plt.plot(test33, test333)
plt.title('Runga Kutta Method: Ts:0.0001')
plt.subplot(122)
plt.plot(testaa, testaaa)
#plt.plot(testbb, testbbb)
plt.plot(testcc, testccc)
plt.title('Eulers Method: Ts: 0.0001')

plt.show()

#Changing step sizes
test1, test11, test111 = rkfunc(1, 0, 0.0005, 2)
test2, test22, test222 = rkfunc(1, 0, 0.0005, 4)
test3, test33, test333 = rkfunc(1, 0, 0.0005, 6)
test4, test44, test444 = rkfunc(1, 0, 0.0005, 8)
test5, test55, test555 = rkfunc(1, 0, 0.0005, 10)

testa, testaa, testaaa = func(1, 0, 0.0005, 2)
testb, testbb, testbbb = func(1, 0, 0.0005, 4)
testc, testcc, testccc = func(1, 0, 0.0005, 6)
testd, testdd, testddd = func(1, 0, 0.0005, 8)
teste, testee, testeee = func(1, 0, 0.0005, 10)

plt.subplot(121)
plt.plot(test11, test111)
plt.plot(test22, test222)
#plt.plot(test33, test333)
plt.title('Runga Kutta Method: Ts:0.0005')
plt.subplot(122)
plt.plot(testaa, testaaa)
#plt.plot(testbb, testbbb)
plt.plot(testcc, testccc)
plt.title('Eulers Method: Ts:0.0005')


