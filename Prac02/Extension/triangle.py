#
# triangle.py - calculates area of triangle
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

###########################################################################################

print("\nTRIANGE AREA\n")

print("              c\n            /\ \n          /    \ \n        /        \      \n      /            \ \n    +---------+ \n  a                  b

xCord1 = 0.0
yCord1 = 0.0
xCord2 = 1.0
yCord2 = 0.0
xCord3 = 0.5
yCord3 = 1.0

base = xCord2 - xCord1
height = yCord3

total = float((base*height)/2)

print(total)

