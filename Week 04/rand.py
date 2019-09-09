#
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


for each_one in range(10):
    new_seq = powerResidue(50)
    plt.plot(new_seq)
    plt.title("Multiple Sequences at same length")




