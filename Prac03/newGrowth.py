#
# newGrowth.py - simulation of unconstrained growth
#
import matplotlib.pyplot as plt

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
times=[0]
pops=[100]

for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    times.append(time)
    pops.append(population)
    print("Time: ", time, "\tGrowth: ", growth, " \tPopulation: ", population)
print("\nPROCESSING COMPLETE.\n")

print("\nTimes: \n", times)
print("\nPops: \n", pops)

plt.title("Unconstrained Growth - Triangles")
plt.plot(times, pops, 'r^')
plt.show()

plt.title("Prac 3.1: Unconstrained Growth")
plt.plot(times, pops, color="green")
plt.show() 
