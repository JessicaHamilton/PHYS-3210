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
    #initialize values for the tree and the basket and set range for turns
    Cherry_tree = 10
    Basket = 0
    #set loop for number of spins
    for turn in range(N):
        #setup if statement to randomly generate a value between 0 and 1 for the weight of the spin
        weight = rand.random()
        if weight >= 0.75:
            spin = rand.randint(4,6)
        else:
            spin = rand.randint(0,3)
        if spin == 0:
            Cherry_tree = Cherry_tree - 1
            Basket = Basket + 1
            if Basket == 10:
                break
        elif spin == 1:
            Cherry_tree = Cherry_tree - 2
            Basket = Basket + 2
            if Basket == 10:
                break
        elif spin == 2:
            Cherry_tree = Cherry_tree - 3
            Basket = Basket + 3
            if Basket == 10:
                break
        elif spin == 3:
            Cherry_tree = Cherry_tree -4
            Basket = Basket + 4
            if Basket == 10:
                break
        elif spin == 4 or spin == 5:
            if Basket < 2 and Basket > 0:
                Cherry_tree = Cherry_tree +1
                Basket = Basket -1
            elif Basket >= 2:
                Cherry_tree = Cherry_tree +2
                Basket = Basket - 2
            else:
                continue
        elif spin == 6:
            length = Basket
            Cherry_tree = Cherry_tree + length
            Basket = 0

        turns_played = turn
        return turns_played
#Print(“The amount of turns it takes to win:”, turns)

def new_cherry(N):

    #initialize values for the tree and the basket and set range for turns
    Cherry_tree = 10
    Basket = 0
    for turns in range(N):
        #randomly generate integers between 0 and 7 to simulate the different options the spinner can land on
        spins = rand.randint(0,6,1)
        #Setup if statement to clarify what happens in each spin, may not actually need for loop!!
        if spins == 0:
            Cherry_tree = Cherry_tree - 1
            Basket = Basket + 1
            if Basket == 10:
                break
        elif spins == 1:
            Cherry_tree = Cherry_tree - 2
            Basket = Basket + 2
            if Basket == 10:
                break
        elif spins == 2:
            Cherry_tree = Cherry_tree - 3
            Basket = Basket + 3
            if Basket == 10:
                break
        elif spins == 3:
            Cherry_tree = Cherry_tree - 4
            Basket = Basket + 4
            if Basket == 10:
                break
        elif spins == 4 or spins == 5:
            if Basket < 2 and Basket >=0:
                Cherry_tree = Cherry_tree + 1
                Basket = Basket - 1
            elif Basket >= 2:
                Cherry_tree = Cherry_tree + 2
                Basket = Basket - 2
            else:
                continue
        elif spins == 6:
            lengths = Basket
            Cherry_tree = Cherry_tree + lengths
            Basket = 0
    turn_played = turns
    return turn_played



test1 = old_cherry(50)
print("Turns for old version:",(test1+1))
test2 = new_cherry(50)
print("Turns for new version:",(test2+1))    

