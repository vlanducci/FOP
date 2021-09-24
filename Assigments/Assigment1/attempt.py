from typing import Counter
import pygame, sys
import numpy as np
import random
from pygame.constants import SRCCOLORKEY
pygame.init()


# ----- Defining Variables ------
loop = True
youngPlayers = []
youngPlayersL = []
adultPlayers = []
adultPlayersL = []
elderlyPlayers = []
elderlyPlayersL = []
deaths = []
screenWidth = 800
screenHeight = 600
boundary = 400
counter = 0
population = 0


screen = pygame.display.set_mode((screenWidth, screenHeight))
youngPlayerImage = pygame.image.load("Goose_portrait.png")
youngPlayerImage = pygame.transform.scale(youngPlayerImage, (50, 50))
adultPlayerImage = pygame.image.load("australianbluetreefrog.png")
adultPlayerImage = pygame.transform.scale(adultPlayerImage, (50, 50))
elderlyPlayerImage = pygame.image.load("crab.png")
elderlyPlayerImage = pygame.transform.scale(elderlyPlayerImage, (50, 50))

# Buttons
smallfont = pygame.font.SysFont('Corbel',35)
addText = smallfont.render('Add Cat' , True , (0,0,0))
predText = smallfont.render('Add Predator' , True , (0,0,0))


# playersNum = int(input("Amount: "))
playersNum = 4  # for testing

for _ in range(playersNum):
    x = random.randint(200,screenWidth-200)
    y = random.randint(200, screenHeight-200)
    cords = str(x) + "," + str(y)
    youngPlayers.append(cords)

for i in youngPlayers:
    split = i.split(',')
    if ',' in split:
        split = split.remove(',')
    youngPlayersL.append(split)


def randomCord(listName, speed):
    for i in listName:
        loopA = True
        x = int(i[0])
        y = int(i[1])
        while loopA:
            xStep = random.randint(0,speed)
            yStep = random.randint(0,speed)
            pOrm = random.randint(0,1)
            if pOrm == 0:
                xtestStep = (int(i[0]) + xStep)
                ytestStep = (int(i[1]) + yStep)
            else:
                xtestStep = (int(i[0]) - xStep)
                ytestStep = (int(i[1]) - yStep)
            if ((xtestStep)>boundary) and ((xtestStep)<screenWidth-boundary) and ((ytestStep)>boundary) and ((ytestStep)<screenHeight-boundary):
                loopA = False
        if pOrm == 0:
            i[0] = str(int(i[0]) + xStep)
            i[1] = str(int(i[1]) + yStep)
        else:
            i[0] = str(int(i[0]) - xStep)
            i[1] = str(int(i[1]) - yStep)


def youngPlayer():
    for i in youngPlayersL:
        screen.blit(youngPlayerImage, ((int(i[0])), (int(i[1]))))


def adultPlayer():
    for i in adultPlayersL:
        screen.blit(adultPlayerImage, ((int(i[0])), (int(i[1]))))
    if len(youngPlayersL) > 0 and counter >= 10:
        young = random.choice(youngPlayersL)
        youngPlayersL.remove(young)
        adultPlayersL.append(young)


def elderlyPlayer():
    for i in elderlyPlayersL:
        screen.blit(elderlyPlayerImage, ((int(i[0])), (int(i[1]))))
    if len(adultPlayersL) > 0 and counter >= 20:
        adult = random.choice(adultPlayersL)
        adultPlayersL.remove(adult)
        elderlyPlayersL.append(adult)
    if len(elderlyPlayersL) > 0 and counter >= 30:
        elderly = random.choice(elderlyPlayersL)
        elderlyPlayersL.remove(elderly)
        deaths.append(1)
        print(sum(deaths))
    

while loop:
    screen.fill((0,0,0))
    counterText = smallfont.render(str(counter) , True , (255,255,255))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(20,150,760,400), 2)
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and 20 <= mouse[0] <= 20 + 140
            and screenHeight - 45 <= mouse[1] <= screenHeight - 45 + 40
        ):
            print("hello")
            population += 1
            x = random.randint(200,screenWidth-200)
            y = random.randint(200, screenHeight-200)
            cords = str(x) + "," + str(y)
            # youngPlayers.append(cords)
            split = cords.split(',')
            if ',' in split:
                split = split.remove(',')
            youngPlayersL.append(split)
            
    pygame.draw.rect(screen,(200,200,200),[20,screenHeight-45,120,40])

    screen.blit(addText , (20,screenHeight-45))
    screen.blit(counterText , (20,20))

    youngPlayer()
    adultPlayer()
    elderlyPlayer()

    randomCord(youngPlayersL, 10)
    randomCord(adultPlayersL, 10)
    randomCord(elderlyPlayersL, 10)

    pygame.time.wait(800)
    pygame.display.update()

    counter += 1
    