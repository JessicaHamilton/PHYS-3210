# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:13:00 2019

@author: hamil
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand

#first function for old version of game
def old_cherry(N):
    #initialize values for tree,basket, and turns
    Cherry_tree = 10
    Basket = 0
    spins = 1
    #set loop for number of spins
    for turn in range(N):
        #setup if statement to randomly generate a value between 0 and 1 for the weight of the spin
        weight = rand.random()
        #If lower - generate spin to increase basket
        if weight <= 0.60:
            spin = rand.randint(0,4)
            #determine what happens with each spin    
            if spin == 0:
                Cherry_tree = Cherry_tree - 1
                Basket = Basket + 1
                if Basket == 10:
                    spins = spins + 1
                    break
            elif spin == 1:
                Cherry_tree = Cherry_tree - 2
                Basket = Basket + 2
                if Basket == 10:
                    spins = spins + 1
                    break
            elif spin == 2:
                Cherry_tree = Cherry_tree - 3
                Basket = Basket + 3
                if Basket == 10:
                    spins = spins + 1
                    break
            elif spin == 3:
                Cherry_tree = Cherry_tree - 4
                Basket = Basket + 4
                if Basket == 10:
                    spins = spins + 1
                    break
                
        #if higher, generate spin to decrease basket       
        elif weight > 0.60:
            #determine what happens with each spin
            spin = rand.randint(4,7)
            if spin == 4 or spin == 5:
                if Basket < 2 and Basket > 0:
                    Cherry_tree = Cherry_tree +1
                    Basket = Basket -1
                    spins = spins + 1
                elif Basket >= 2:
                    Cherry_tree = Cherry_tree +2
                    Basket = Basket - 2
                    spins = spins + 1
                else:
                    spins = spins + 1
                    continue
            elif spin == 6:
                Cherry_tree = Cherry_tree + Basket
                Basket = 0
                spins = spins + 1
    return spins

def new_cherry(N):

    #initialize values for the tree and the basket and set range for turns
    Cherry_tree = 10
    Basket = 0
    spins2 = 0
    for t in range(N):
        #randomly generate integers between 0 and 7 to simulate the different options the spinner can land on
        spinnn = rand.randint(0,7)
        #Setup if statement to clarify what happens in each spin, may not actually need for loop!!
        if spinnn == 0:
            Cherry_tree = Cherry_tree - 1
            Basket = Basket + 1
            spins2 = spins2 + 1
            if Basket == 10:
                break
        elif spinnn == 1:
            Cherry_tree = Cherry_tree - 2
            Basket = Basket + 2
            spins2 = spins2 + 1
            if Basket == 10:
                break
        elif spinnn == 2:
            Cherry_tree = Cherry_tree - 3
            Basket = Basket + 3
            spins2 = spins2 + 1
            if Basket == 10:
                break
        elif spinnn == 3:
            Cherry_tree = Cherry_tree - 4
            Basket = Basket + 4
            spins2 = spins2 + 1
            if Basket == 10:
                break
        elif spinnn == 4 or spinnn == 5:
            if Basket < 2 and Basket >=0:
                Cherry_tree = Cherry_tree + 1
                Basket = Basket - 1
                spins2 = spins2 + 1
            elif Basket >= 2:
                Cherry_tree = Cherry_tree + 2
                Basket = Basket - 2
                spins2 = spins2 + 1
            else:
                spins2 = spins2 + 1
                continue
        elif spinnn == 6:
            Cherry_tree = Cherry_tree + Basket
            Basket = 0
            spins2 = spins2 + 1
    return spins2



old_array = []
new_array = []
for each_num in range(10):
    test1 = old_cherry(30)
    old_array.append(test1)
    test2 = new_cherry(30)
    new_array.append(test2)
    
average1 = np.average(old_array)
average2 = np.average(new_array)
print("Average number of Turns for old version:",average1)   
print("Average number of Turns for new version:",average2)    
    
    
    
    
    