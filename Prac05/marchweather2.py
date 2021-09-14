#
# marchweather2.py - read in values and plots them
#                   
# (source: "http://www.bom.gov.au/climate/dwo/202103/html/IDCJDW6111.202103.shtml")
#

import matplotlib.pyplot as plt

fileobj = open("marchweatherfull.csv", "r")
data = fileobj.readlines()
fileobj.close()

mins = [] # do the same for maxs, nines and threes
maxs = []
nines = []
threes = []

for line in data:
    splitline = line.split(",")
    mins.append(splitline[2])
    maxs.append(splitline[3])
    nines.append(splitline[10])
    threes.append(splitline[16])

print("\n",mins)
print("\n",maxs)
print("\n",nines)
print("\n",threes)

dates = range(1,32)

plt.plot(dates, mins, dates, maxs, dates, nines, dates, threes)
plt.show()
