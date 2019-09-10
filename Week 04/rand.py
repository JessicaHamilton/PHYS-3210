#
import numpy as np
import matplotlib.pyplot as plt

def powerResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    import datetime
    if seed == None:
        #print("Seed value set to NONE, defaulting to system time.")
        seed=int(datetime.datetime.now().strftime("%Y%M%d%H%M%S"))
    else:
        pass

    r = seed
    rand = []
    for i in range(N):
        rand.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    return rand[0:N]




#Generate a seq of random numbers and print them, also plotted
first_seq = powerResidue(50)
print(first_seq)
x_values = np.arange(0,50)
plt.plot(x_values, first_seq)
plt.title("First Sequence Test")
plt.show()
#The list when printed seems somewhat random 

#Change value of constants and seed value to produce a sequence that repeats itself
#We can change the values of a and M to see if we can get a repeating pattern
#Initial values
#a = 273673163155
#M = 2**48

second_seq = powerResidue(50,a=27367, M=2**12)
print(second_seq)

plt.plot(x_values, second_seq)
plt.title("Second Sequence Test with Changes in a and M")
plt.show()


#Now change the seed value to see if we can produce a sequence that repeats itself
third_seq = powerResidue(50,seed=9729834523)
print(third_seq)
plt.plot(x_values, third_seq)
plt.title("Third Sequence Test with Changes in Seed")
plt.show()

#Now change all three values to see if we can produce a seq that repeats
fourth_seq = powerResidue(50, seed=987087257133932, a=273, M=2**4)
print(fourth_seq)
plt.plot(x_values, fourth_seq)
plt.title("Fourth Sequence Test Looking for Patterns")
plt.show()

def new_pResidue(N, seed=None, a=273673163155, c=13, M=2**48):
    """ Calculate a series of random numbers
    """
    #import datetime
    #if seed == None:
        #print("Seed value set to NONE, defaulting to system time.")
        #seed=int(datetime.datetime.now().strftime("%Y%M%d%H%M%S"))
    #else:
        #seed = seed + 23
    r = seed
    rand = []
    for i in range(N):
        rand.append(((a*r + c) % M)/M)
        r = (a*r + c) % M
    return rand[0:N]

import datetime
seed = seed=int(datetime.datetime.now().strftime("%Y%M%d%H%M%S"))
for each_one in range(4):
    new_seq = new_pResidue(50,seed)
    seed = seed+23
    plt.plot(new_seq)
    plt.title("Multiple Sequences at same length")
    
plt.show()
#When looking at the plot with multiple sequences, There seems to be random sequences
    #when you look closer, you can notice there are times in all of the sequences that
    #each tend to drop in values or climb in values. Otherwise the sequences seem to vary
    #in decreasing or increasing successive values and their severity of the jumps as well.
    
#To try and fix the times where all sequences tend to drop in values at the same time, we can
    #try changing the values of the constants. Seems like increasing a and M worked, or at least
    #made it difficult to see a pattern.
for each_one in range(4):
    new_seq = new_pResidue(50,seed, a=70928509284734092, M=7**48)
    seed = seed+23
    plt.plot(new_seq)
    plt.title('Fixed Multiple Sequences at same length')

plt.show()

#Now use the numpy random function and scatter-plot against this function to see difference
xvalues = np.arange(0,75)
random_values = np.random.random(75)
our_values = powerResidue(75)
plt.scatter(xvalues,random_values,s=2, color = "blue", label="Numpy Function")
plt.scatter(xvalues,our_values,s=2, color = "red", label="Our Function")
plt.title("Numpy Random function versus Our function")
plt.xlim(0,80)
plt.ylim(0.0,1.25)
plt.legend()

#When looking at the distribution of values for the numpy random function and our function
#I believe our function almost seems better at the "randomness" Our function does not seem
#to have as many values clumped together like the numpy function does. There seems to be 
#a more uniform distribution to the values for our function. THen again, uniform is not necessarily 
#random, and random values can occur in clumps. So perhaps with that point stated, numpy
#function could actually be better at generating random values.









