#
#  growth.py - simulation of unconstrained growth
#

print("\nSIMULATION - Unconstrained Growth\n")

length = 10
population = 100
growthRate = 0.1
timeStep = 0.5
numIter = length / timeStep
growthStep = growthRate * timeStep

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growthRate)
print("Time Step (part hour per step): ", timeStep)
print("Num iterations (sim length * time step per hour): ", numIter)
print("Growth step (growth rate per time step): ", growthStep)

print("\nResult:\n")

print("Time: ", 0, "\tGrowth: ", 0, " \tPopulation: ", 100)

for i in range (1, int(numIter) + 1 ):
    growth = growthStep * population
    population = population + growth
    time = i * timeStep
    print("Time: ", time, " \tGrowth: ", growth, " \tPopulation: ", population)

print("\nPROCESSING COMPLETE.\n")

