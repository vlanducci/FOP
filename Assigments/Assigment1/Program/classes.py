#
#
#

from typing import Counter
import pygame, sys
import numpy as np
import random

boundary = 200
screenWidth = 800
screenHeight = 600

class Cats():
    def __init__(self, x, y, speed, attitude, counter, sleepCounter, sleep, hungry, hungryCounter, birthCounter, closest, closestDone):
        self.x = x
        self.y = y
        self.speed = speed
        self.attitude = attitude
        self.counter = counter
        self.sleepCounter = sleepCounter
        self.sleep = sleep
        self.hungry = hungry
        self.hungryCounter = hungryCounter
        self.birthCounter = birthCounter
        self.closest = closest
        self.closestDone = closestDone


    def randomCordClass(self, x, y, speed):
        loopA = True
        if (int(self.speed) <= 1):
            self.speed = 3
        while loopA:
            if self.sleep == True:
                loopA = False
            if (((x - 200 < 60 and (x - 200) > 0) or ((200 - x < 60) and (200 - x > 0))) and (y - 250 < 60 and (y - 200 > 0) or ((250 - y < 20) and 250 - y > 0))):
                speed = 1
                xStep = speed
                yStep = speed
            else:
                xStep = random.randint(2,speed)
                yStep = random.randint(2,speed)
            pOrm = random.randint(0,1)
            if pOrm == 0:
                xtestStep = x + xStep
                ytestStep = y + yStep
            else:
                xtestStep = x - xStep
                ytestStep = y - yStep
            if ((xtestStep)>30) and ((xtestStep)<730) and ((ytestStep)>150) and ((ytestStep)<500):
                self.x = str(xtestStep)
                self.y = str(ytestStep)
                loopA = False

class YoungCat(Cats):
    myclass = "Young Cat"

class AdultCat(Cats):
    myclass = "Adult Cat"

class ElderlyCat(Cats):
    myclass = "Elderly Cat"

class Predator():
    def __init__(self, x, y,counter):
        self.x = x
        self.y = y
        self.counter = counter

    def randomCordClass(self, x, y):
        loopA = True
        while loopA:
            xStep = random.randint(0,20)
            yStep = random.randint(0,20)
            pOrm = random.randint(0,1)
            if pOrm == 0:
                xtestStep = x + xStep
                ytestStep = y + yStep
            else:
                xtestStep = x - xStep
                ytestStep = y - yStep

            if ((xtestStep)>boundary) and ((xtestStep)<screenWidth-boundary) and ((ytestStep)>boundary) and ((ytestStep)<screenHeight-boundary):
                self.x = str(xtestStep)
                self.y = str(ytestStep)
                loopA = False

class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y