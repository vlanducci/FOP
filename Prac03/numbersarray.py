#
# numbersarray.py: Read ten numbers give sum, min, max & mean
#

import numpy as np
import matplotlib.pyplot as plt

numarray = np.zeros(10) # create an empty 10 element array

print('Enter ten numbers: ')

for i in range(len(numarray)):
    print('Enter a number (', i + 1, '): ')
    numarray[i] = int(input())

numSum = numarray.sum()
numMin = numarray.min()
numMax = numarray.max()
numMean = numarray.mean()

print('Total is ', numarray.sum())
print("Min is ", numarray.min())
print("Max is ", numarray.max())
print("Mean is ", numarray.mean())

plt.title("Entered Numbers")
plt.plot(numarray)
plt.show() 
