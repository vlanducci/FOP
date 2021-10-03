#
#
#

from typing import Counter
import pygame, sys
import numpy as np
import random

boundary = 60
screenWidth = 800
screenHeight = 600

class Cats():
    def __init__(self, x, y, speed, jump, attitude, counter, sleepCounter, sleep):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump = jump
        self.attitude = attitude
        self.counter = counter
        self.sleepCounter = sleepCounter
        self.sleep = sleep

    def randomCordClass(self, x, y, speed):
        loopA = True
        while loopA:
            if self.sleep == True:
                loopA = False

            xStep = random.randint(0,speed)
            yStep = random.randint(0,speed)
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

class YoungCat(Cats):
    myclass = "Young Cat"

class AdultCat(Cats):
    myclass = "Adult Cat"

class ElderlyCat(Cats):
    myclass = "Elderly Cat"