# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:02:58 2019

@author: hamil
"""

#Please see exercise04 and associated documents for the coding part of this exercise/problem
#Derivation of equation 4: N_v = Xe^(-k_1t) + (N_v0-X)e^-k_vt



#First we need to define the variables which will be used. 
#N_I(t) = number of infected T cells at time t
#N_V(t) = number of free virions in the blood (viral load)
#t = time
#k_I = constant
#When we have a group of infected T-cells they produce virions which will infect new cells. This is speaking
#to the rate at which 