#video on the topic: https://www.youtube.com/watch?v=n8SRgLD3DC8
#thanks to Flammable Maths for that very interesting video
import random

l = float(input("Enter the total lenght of the object:\t"))
n = int(input("How many parts should be divided into?\t"))
s = float(input("Enter the exponent for the significance level 10^s\t: s = "))
s = 10**(s)
d = random.uniform(l/2,l) #guesses a random float in the interval [l/2,l] \approx 1/n
i = 1
if not d == l and l/2: #checks if d is unequal to l and l/2
    while not ((l/n)-s < d < (l/n)+s): #d != 1/n:
        ld_diff = l - d
        d = ld_diff/(n-1) # \approx (1-1/n)/(n-1)
        print(d) #can be uncommented if every value for d should be shown
        i += 1
    print("The estimated value of",l,"/",int(n), "after ",i, "run(s) is", d,".")
    print("In fact l/n is",l/n,".")
else:
    print("Please run again.")
