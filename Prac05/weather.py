#
# weather.py: Print min and max temps from a file
#
#   (source: http://www.bom.gov.au/climate/)
#

import matplotlib.pyplot as plt

fileobj = open("marchweather.csv", "r")

print("\n\n")
line1 = fileobj.readline()
line2 = fileobj.readline()
line1 = line1.replace('\n', '')
xLinelist = line1.split(',')
yLinelist = line2.split(',')
print(xLinelist)
print(yLinelist)
print("\n\n")

fileobj.close()


mins = xLinelist # add splitting code here
maxs = yLinelist # add splitting code here
dates = range(1,32)

plt.plot(dates, mins, dates, maxs)
plt.show()
