import random
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

class Bubble():
    size = 20
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.randint(1,4) * random.choice([1,-1])
        self.dy = random.randint(1,4) * random.choice([1,-1])
        self.life = random.randint(10,15)
        
    def getstate(self):
        return (self.x, self.y, self.size, self.life)
        
    def tic(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

def bplot(b, s):
    plt.scatter(b, s, s=sizes)
    plt.xlim(0,size-1)
    plt.ylim(0,size-1)
    plt.pause(1)
    plt.clf()

size = int(input("size: "))
numbubbles = int(input("number of bubbles: "))

bubbles = []
for i in range(numbubbles):
    bubbles.append(Bubble(size/2, size/2))

totalPop = 0
totalDep = 0
count = 0

xvalues = [b.getstate()[0] for b in bubbles]
yvalues = [b.getstate()[1] for b in bubbles]
bplot(xvalues, yvalues)

while bubbles:
    popped = []
    for i in range(len(bubbles)):
        b = bubbles[i]
        b.tic()
        gone = False
        state = b.getstate()
        if state[0] < 0 or state[0] >= size or state[1] < 0 or state[1] >= size:
            print("departed")
            gone = True
            totalDep += 1
        if state[3] < 0:
            print("pop!!")
            gone = True
            totalPop += 1
        if gone:
            popped.append(i)
    for j in range(len(popped)-1,-1, -1):
        bubbles.pop(popped[j])
    xvalues = [b.getstate()[0] for b in bubbles]
    yvalues = [b.getstate()[1] for b in bubbles]
    sizes = [b.getstate()[2] for b in bubbles]
    bplot(xvalues,yvalues)
    count +=1

print("Number of pops: " + str(totalPop))
print("number of drifts: " + str(totalDep))
print("number of iterations before all gone: " + str(count))