#
# darts.py - calculates if dart hits circle
#

import random
numTrials = 1000000

ncirc = 0
r = 1.0 # radius of circle
r2 = r*r

for i in range(numTrials):
    x = random.random();
    y = random.random();
    if ((x*x + y*y) <= r2):
        ncirc += 1

pi = 4.0 * ncirc/ numTrials

print("\nFor ", numTrials, " trials, pi = ", pi)

