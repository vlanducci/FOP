#
# Name : <student name>
# ID   : <student ID>
#
# heat.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

size = 10 

def calcheat(subarray):
    result = 0.1 * (subarray.sum() + subarray[1,1])
    return result

curr = np.zeros((size,size)) 
print(curr)

# create heat source
hlist = []
fileobj = open('heatsource.csv','r')
for line in fileobj:
    line_s = line.strip()
    ints = [int(x) for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()

harray = np.array(hlist, dtype=int)
curr = harray.copy()

next = np.zeros((size,size)) 

# Calculate heat diffusion
for timestep in range(100):
    for r in range(1,size-1):
        for c in range (1, size-1):
            next[r,c]=calcheat(curr[r-1:r+2,c-1:c+2])
    next = np.where(harray>next, harray, next)

    curr = next.copy()

plt.imshow(curr, cmap=plt.cm.hot) 
plt.show() 
