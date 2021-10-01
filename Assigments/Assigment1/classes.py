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

class YoungCat():
    def __init__(self, x, y, speed, jump, attitude, counter):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump = jump
        self.attitude = attitude
        self.counter = counter

    def randomCordClass(self, x, y, speed):
        loopA = True
        while loopA:
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

class AdultCat():
    def __init__(self, x, y, speed, jump, attitude, counter):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump = jump
        self.attitude = attitude
        self.counter = counter

    def randomCordClass(self, x, y, speed):
        loopA = True
        while loopA:
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

class ElderlyCat():
    def __init__(self, x, y, speed, jump, attitude, counter):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump = jump
        self.attitude = attitude
        self.counter = counter

    def randomCordClass(self, x, y, speed):
        loopA = True
        while loopA:
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