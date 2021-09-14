#
# test2.py - extend this code with arrays and plotting
#
# Student Name : Viola Landucci
# Student ID   : 20769446
#

import matplotlib.pyplot as plt
import numpy as np

plots = 24

def showdata(title, x, y, s, c):
    print("\n==="+title+"===\n")
    print("xvalues: "+ str(x))
    print("yvalues: "+ str(y))
    print("sizes: "+str(s))
    print("colours: "+str(c))


# set up x and y values for scatterplot

xlist = [0,1,2,3,4,5]          # list to build x values
xvalues = np.array(xlist*4)    # 0-5 repeating
yvalues = np.arange(0,plots,1)  # 0-(plots-1)
yvalues = yvalues // 6         # 6*0, 6*1... 6*5

# set up colours and sizes for plot 1

sizes1 = np.full(plots, 100)
colours1 = np.ones(plots)       # colours for plot 1
sizes2 = np.full(plots, 100)
colours2 = np.ones(plots)

sizes1[::4] = 200
sizes1[1::4] = 150
sizes1[2::4] = 250
sizes1[3::4] = 100

colours1[::4] = 30
colours1[1::4] = 10
colours1[2::4] = 20
colours1[3::4] = 10

sizes2[::4] = 200*30
sizes2[1::4] = 150*30
sizes2[2::4] = 250*30
sizes2[3::4] = 100*30

colours2[::3] = 40
colours2[1::3] = 50
colours2[2::3] = 60

showdata("PLOT 1", xvalues, yvalues, sizes1, colours1)

plt.figure(1)
plt.subplot(211)
plt.title("Plot 1", fontsize=18, fontweight='bold')
plt.xlabel("x values")
plt.ylabel("y values")
print(colours1)
plt.scatter(xvalues, yvalues, s=sizes1, c=colours1)
plt.colorbar()


###################################

showdata("PLOT 2", xvalues, yvalues, sizes2, colours2)

plt.subplot(212)
plt.title("Plot 2", fontsize=18, fontweight='bold')
plt.xlabel("x values")
plt.ylabel("y values")
plt.scatter(xvalues, yvalues, s=sizes2, c=colours2, alpha=0.5, cmap='plasma')
plt.colorbar()
plt.show()

