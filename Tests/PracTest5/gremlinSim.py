'''

gremlin_sim.py - gremlin simulation, based on three rules and random movement

Rules:
    First of all, keep him out of the light, he hates bright light, 
        especially sunlight, it'll kill him. 
    Second, don't give him any water, not even to drink. 
    But the most important rule, the rule you can never forget, 
        no matter how much he cries, no matter how much he begs, 
        never feed him after midnight. 

Prac Test 5 - base or experiment code for Parameter Sweep

'''

import matplotlib.pyplot as plt
import numpy as np
import random

MAXROW = 20
MAXCOL = 30

def move_em(current, moves):
    nextgrid = np.zeros(current.shape, dtype="int16")
    
    for row in range(MAXROW):
        for col in range(MAXCOL):
            for g in range(current[row,col]):
                nextrow = row + random.choice(moves)
                nextcol = col + random.choice(moves)
                #print("Newpos = ", nextrow, nextcol)
                if nextrow < 0:
                    nextrow = 0
                if nextcol < 0:
                    nextcol = 0
                if nextrow >= MAXROW:
                    nextrow = MAXROW - 1
                if nextcol >= MAXCOL:
                    nextcol = MAXCOL - 1
                nextgrid[nextrow, nextcol] += 1
    return nextgrid

def rule1(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    pop[row, col] -= 1
                    print("Less gremlins")                 
                    
def rule2(pop, waterlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in waterlist:
                for g in range(pop[row,col]):
                    pop[row, col] += 1
                    print("More gremlins")
    
def rule3(good, evil, foodlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in foodlist and good[row, col] > 0:
                print(good[row, col], "Gremlins turned evil")
                evil[row, col] += good[row, col]
                good[row, col] += 0

def make_map(itemlist, colour):
    xlist = []
    ylist = []
    for r,c in itemlist:
        ylist.append(MAXROW - r - 1)  
        xlist.append(c) 
    plt.scatter(xlist,ylist,color=colour, marker='s')
    
def make_scatter(pop, colour):
    xlist = []
    ylist = []
    slist = []
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if pop[row,col] > 0:
                ylist.append(MAXROW - row - 1)  
                xlist.append(col) #flip rows/columns to y/x
                slist.append(pop[row,col]*20)
    plt.scatter(xlist,ylist,s=slist,color=colour)
  

def main():

    goodarray = np.zeros((MAXROW,MAXCOL), dtype="int16")
    evilarray = np.zeros((MAXROW,MAXCOL), dtype="int16")

    water = [(19,2),(18,2),(17,2),(16,2),(2,27),(3,27),(4,27),(5,27)]
    light = [(19,0),(18,0),(17,0),(16,0),(19,25),(18,26),(17,27),(16,28),(15,29)]
    food  = [(10,10),(5,5),(5,15),(15,5),(5,10),(10,5),(15,15),(15,10),(10,15),(5,20),(10,20),(15,20),
             (5,25),(10,25),(15,25)]
    g_moves  = [-1,0,1]
    e_moves  = [-2,-1,0,1,2]

    # Starting population
    initpop = 10
    
    for i in range(initpop):  # add good gremlins to grid
        goodarray[random.randint(0,MAXROW-1),random.randint(0,MAXCOL-1)] += 1 

    # Simulation
    
    for t in range(30):    # @ 8 hour / timestep = 10 days
        print("### Timestep ", t, "###")
        goodnext = move_em(goodarray, g_moves)
        evilnext = move_em(evilarray, e_moves)
        
        rule1(goodnext, light)
        rule1(evilnext, light)
        rule2(goodnext, water)
        rule2(evilnext, water)
        if t%3 == 0:       # after midnight till 8am
            rule3(goodnext, evilnext, food)
        
        goodarray = goodnext
        evilarray = evilnext
        
        make_scatter(goodarray, "b")
        make_scatter(evilarray, "r")
        make_map(water, "c")
        make_map(light, "y")
        make_map(food, "g")
        plt.title("Gremlin Simulation (time = " + str(t) + ")")
        plt.xlabel("Columns")
        plt.ylabel("Rows")
        plt.xlim(-1,MAXCOL)
        plt.ylim(-1,MAXROW)
        plt.pause(1)
        plt.clf()
    
if __name__ == "__main__":
    main()
