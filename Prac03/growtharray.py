#
# growtharray.py - plotting growth with arrays
#

import matplotlib.pyplot as plt
import numpy as np

print("\nSIMULATION - Unconstrained Growth\n")
length = 1000
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (length * timestep / hour):",num_iter)
print("Growth step (growthrate per timestep):",growth_step)


print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
timesarray = np.array([])
popsarray = np.array([])

for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    print("Time: ", time, "\tGrowth: ", growth, " \tPopulation: ", population)
    timesarray = np.append(timesarray, time)
    popsarray = np.append(popsarray, population)
    
print("\nPROCESSING COMPLETE.\n")

plt.title("Unconstrained Growth")
plt.plot(timesarray, popsarray)
plt.show() 
