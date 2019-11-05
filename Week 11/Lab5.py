# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 10:02:22 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt


def rkfunc(x_int, v_int, h, P):
    k = 20
    m = 1
    g = 9.8
    mu_s = 0.1
    mu_k = 0.1
    x_array = []
    v_array = []
    #create initial steps
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10, h)
    for t in time:
        #define forces and variables:
        vmag1 = abs(vnew)
        f_static1 = -mu_s*m*g
        f_kin1 = -mu_k*m*g*(vnew/vmag1)
        f_resto = -k*(xnew**(P-1))
        
        #calculate half steps
        if abs(vnew) < 1e-16:
            v_half = vnew + (f_resto/m + f_static1/m)*(h/2)
        else:
            v_half = vnew + (f_resto/m + f_kin1/m)*(h/2)
        x_half = xnew + vnew*(h/2)
        
        #redefine func and update x and v values for full steps
        vmag2 = abs(v_half)
        f_static2 = -mu_s*g*m
        f_kin2 = -mu_k*g*m*(v_half/vmag2)
        f_resto2 = -k*(x_half**(P-1))
        
        if abs(vnew) < 1e-16:
            vnew = vnew + (f_resto2/m + f_static2/m)*h
        else:
            vnew = vnew + (f_resto2/m + f_kin2/m)*h
        xnew = xnew + h*(v_half)
        
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
        
        if vnew == 0:
            if f_rest > f_static:
                continue
            else:
                break
    return v_array, x_array, time


test1, test11, test111 = rkfunc(1, 1e-16, 0.0001, 2)
test2, test22, test222 = rkfunc(1, 1e-16, 0.0001, 4)
plt.subplot(121)
plt.plot(test11, test111)
plt.plot(test22, test222)
plt.title('Position vs. time: RK')
plt.xlabel('Position')
plt.ylabel('time')
plt.subplot(122)
plt.plot(test1, test111)
plt.plot(test2, test222)
plt.title('Velocity vs. time:RK')
plt.xlabel('Velocity')
plt.ylabel('time')
plt.show()


def func(x_int, v_int, h,P):
    k = 20
    m = 1
    g = 9.8
    mu_s = 0.1
    mu_k = 0.1
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(0,10,h)
    for t in time:
        #update values
        vmag1 = abs(vnew)
        f_static1 = -mu_s*m*g
        f_kin1 = -mu_k*m*g*(vnew/vmag1)
        f_resto = -k*(xnew**(P-1))
        if abs(vnew) < 1e-16:
            vnew = vnew + (f_resto/m + f_static1/m)*h
        else:
            vnew = vnew + (f_resto/m + f_kin1/m)*h
        
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time

testa, testaa, testaaa = func(1, 1e-16, 0.0001, 2)
testb, testbb, testbbb = func(1, 1e-16, 0.0001, 4)
plt.subplot(121)
plt.plot(testaa, testaaa)
plt.plot(testbb, testbbb)
plt.title('Position vs. time: Euler')
plt.xlabel('Position')
plt.ylabel('time')
plt.subplot(122)
plt.plot(testa, testaaa)
plt.plot(testb, testbbb)
plt.title('Velocity vs. time: Euler')
plt.xlabel('Velocity')
plt.ylabel('time')
plt.show()


def crit_func(x_int, v_int, h,P):
    k = 20
    m = 1
    g = 9.8
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(1,10,h)
    for t in time:
        #update values
        b = 2*m*(np.pi/t)
        f_visc = -b*vnew
        f_resto = -k*(xnew**(P-1))
        if abs(vnew) < 1e-16:
            vnew = vnew + (f_resto/m + f_visc/m)*h
        else:
            vnew = vnew + (f_resto/m + f_visc/m)*h
        
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time

def overdamp_func(x_int, v_int, h,P):
    k = 20
    m = 1
    g = 9.8
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(1,10,h)
    for t in time:
        #update values
        b = 2*m*(2*np.pi/t) + 15
        f_visc = -b*vnew
        f_resto = -k*(xnew**(P-1))
        if abs(vnew) < 1e-16:
            vnew = vnew + (f_resto/m + f_visc/m)*h
        else:
            vnew = vnew + (f_resto/m + f_visc/m)*h
        
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time

def underdamp_func(x_int, v_int, h,P):
    k = 20
    m = 1
    g = 9.8
    x_array = []
    v_array = []
    
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(1,10,h)
    for t in time:
        #update values
        b = 2*m*(2*np.pi/t) - 2.5
        f_visc = -b*vnew
        f_resto = -k*(xnew**(P-1))
        if abs(vnew) < 1e-16:
            vnew = vnew + (f_resto/m + f_visc/m)*h
        else:
            vnew = vnew + (f_resto/m + f_visc/m)*h
        
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time


r, rr, rrr = crit_func(1,1e-16,0.0001,2)
j,jj,jjj = overdamp_func(1,1e-16,0.0001,2)
v,vv,vvv = underdamp_func(1,1e-16,0.0001,2)

plt.subplot(131)
plt.plot(rr,rrr)
plt.title('critically damped')
plt.subplot(132)
plt.plot(jj,jjj)
plt.title('Overdamped')
plt.subplot(133)
plt.plot(vv,vvv)
plt.title('Underdamped')
plt.show()
#Now to look into adding driving forces


def rk_drivefunc(x_int, v_int, h, P, omega_o):
    k = 10
    m = 2
    g = 9.8
    f_o = 15
    x_array = []
    v_array = []
    freq_diff_array = []
    #create initial steps
    xnew = x_int
    vnew = v_int
    time = np.arange(0,80,h)
    for t in time:
        #define forces and variables:
        f_resto = -k*(xnew**(P-1))
        f_drive = f_o*np.sin(omega_o*(t))
        #calculate half steps
        v_half = vnew + (f_resto/m + f_drive/m)*(h/2)
        x_half = xnew + vnew*(h/2)
        
        #redefine func and update x and v values for full steps
        f_resto2 = -k*(x_half**(P-1))
        f_drive = f_o*np.sin(omega_o*(t))
        #calculate full steps
        vnew = vnew + (f_resto2/m + f_drive/m)*h
        xnew = xnew + (v_half)*h
        
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
        omega = np.sqrt(k/m)
        
    return v_array, x_array, time, omega, omega_o

ww, www, wwww, wwwww, wwwwww = rk_drivefunc(1, 1e-16, 0.0001, 2, 2)
plt.plot(www, wwww)
plt.title('Position versus Time: Driving Force')
plt.show()

plt.plot(ww, wwww)
plt.title('Velocity versus Time: Driving Force')
plt.show()
diff = wwwww - wwwwww
beat_freq = diff / (2*np.pi)
print('Beat Frequency:', beat_freq)

#Now to vary the freq of the driving force from w_o/10 to 10*w_o
amp_array = []
n_array = []
for n in range(10):
    d,dd,ddd,dddd,ddddd = rk_drivefunc(1,1e-16,0.001,2,2*n)
    n_array.append(2*n)
    x_max = np.max(dd)
    amp_array.append(x_max)
    
plt.plot(n_array, amp_array)
plt.title('Amplitude versus Driving Frequency')
plt.xlabel('Driving Omega')
plt.ylabel('Amplitude')
plt.show()
        
#explore what occurs when a nonlinear sys resonates...

#Add in viscous friction and check the amplitude vs. driver freq again
def crit_drivefunc(x_int, v_int, h,P,omega_o):
    k = 20
    m = 2
    g = 9.8
    x_array = []
    v_array = []
    f_o = 15 
    #create initial step
    xnew = x_int
    vnew = v_int
    time = np.arange(1,10,h)
    for t in time:
        #update values
        b = 2*m*(np.pi/t)
        f_visc = -b*vnew
        f_resto = -k*(xnew**(P-1))
        f_drive = f_o*np.sin(omega_o*(t))
        if abs(vnew) < 1e-16:
            vnew = vnew + (f_resto/m + f_visc/m + f_drive/m)*h
        else:
            vnew = vnew + (f_resto/m + f_visc/m + f_drive/m)*h
        
        xnew = xnew + vnew*h
        #append to arrays
        v_array.append(vnew)
        x_array.append(xnew)
    return v_array, x_array, time

amp_array = []
n_array = []
for n in range(10):
    g,gg,ggg = crit_drivefunc(1,1e-16,0.001,2,2*n)
    n_array.append(2*n)
    x_max = np.max(gg)
    amp_array.append(x_max)


plt.plot(n_array, amp_array)
plt.title('Amplitude versus Driving Frequency with Friction')
plt.xlabel('Driving Omega')
plt.ylabel('Amplitude')
plt.show()

#now vary p with the driving force
p_array = np.arange(2,12,2)
for p in p_array:
    h,hh,hhh,hhhh,hhhhh = rk_drivefunc(1,1e-16,0.0001,p,2)
    plt.plot(hh,hhh)
    plt.title('Position versus Time varying P')
    



