from typing import Counter
import pygame, sys
import numpy as np
import random
from pygame.constants import SRCCOLORKEY
from classes import *
pygame.init()


# ----- Defining Variables ------
loop = True
deaths = []
young = []
adult = []
elderly = []
cat = []
predator = []
youngRemove = []
adultRemove = []
elderlyRemove = []
counter = 0
population = 0
day = 1
youngCap = 0
killed = 0
DorN = ""


def sleep(list, chance):
    for i in range(len(list)):
        YorN = random.randint(0, chance)
        if YorN == 0:
            list[i].sleep = True
            list[i].sleepCounter = 0

def predKill(list, killList):
    for i in range(len(predator)):
        for e in range(len(list)):
            if ((int(list[e].x) - int(predator[i].x) < 20 and (int(list[e].x) - int(predator[i].x) > 0) or ((int(predator[i].x) - int(list[e].x) < 20) and (int(predator[i].x) - int(list[e].x) > 0))) and (int(list[e].y) - int(predator[i].y) < 20 and (int(list[e].y) - int(predator[i].x) > 0) or ((int(predator[i].y) - int(list[e].y) < 20) and (int(predator[i].y) - int(list[e].y) > 0)))):
                if list[e] not in killList:
                    killList.append(list[e])


screen = pygame.display.set_mode((screenWidth, screenHeight))
youngPlayerImage = pygame.image.load("Goose_portrait.png")
youngPlayerImage = pygame.transform.scale(youngPlayerImage, (50, 50))
adultPlayerImage = pygame.image.load("australianbluetreefrog.png")
adultPlayerImage = pygame.transform.scale(adultPlayerImage, (50, 50))
elderlyPlayerImage = pygame.image.load("crab.png")
elderlyPlayerImage = pygame.transform.scale(elderlyPlayerImage, (50, 50))
predatorImage = pygame.image.load("imposter.png")
predatorImage = pygame.transform.scale(predatorImage, (50, 50))


# Buttons
smallfont = pygame.font.SysFont('Corbel',35)
addText = smallfont.render('Add Cat' , True , (0,0,0))
predText = smallfont.render('Add Predator' , True , (0,0,0))


# playersNum = int(input("Amount: "))
playersNum = 4  # for testing


for _ in range(playersNum):
    x = random.randint(200,screenWidth-200)
    y = random.randint(200, screenHeight-200)
    speed = random.randint(2,10)
    jump = random.randint(2,10)
    attitude = random.randint(0,1)
    cords = str(x) + "," + str(y)
    cat = YoungCat(x,y,speed,jump,attitude, 0, 4, False)
    young.append(cat)


while loop:
    # Counter, Population and Day Counter and determiner 
    population = len(young)+len(adult)+len(elderly)
    counter += 1

    day += 1
    if day > 11:
        day = 0
    if day <= 6:
        DorN = "Day"
        sleep(young, 5)
        sleep(adult, 5)
        sleep(elderly, 5)
    else:
        DorN = "Night"
        sleep(young, 1)
        sleep(adult, 4)
        sleep(elderly, 2)


    # Setting up screen, buttons and text
    if DorN == "Night":
        screen.fill((0,0,0))
        counterText = smallfont.render(str(counter) , True , (255,255,255))
        DorNText = smallfont.render(DorN , True , (255,255,255))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(20,150,760,400), 2)
    if DorN == "Day":
        screen.fill((255,255,255))
        counterText = smallfont.render(str(counter) , True , (0,0,0))
        DorNText = smallfont.render(DorN , True , (0,0,0))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(20,150,760,400), 2)

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and 20 <= mouse[0] <= 20 + 140
            and screenHeight - 45 <= mouse[1] <= screenHeight - 45 + 40
        ):
            x = random.randint(200,screenWidth-200)
            y = random.randint(200, screenHeight-200)
            speed = random.randint(2,10)
            jump = random.randint(2,10)
            attitude = random.randint(0,1)
            cords = str(x) + "," + str(y)
            cat = YoungCat(x,y,speed,jump,attitude, 0, 4, False)
            young.append(cat) 
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and 150 <= mouse[0] <= 150 + 140
            and screenHeight - 45 <= mouse[1] <= screenHeight - 45 + 40
        ):
            x = random.randint(200,screenWidth-200)
            y = random.randint(200, screenHeight-200)
            pred = Predator(x,y,0)
            predator.append(pred) 
    # Add Button
    pygame.draw.rect(screen,(200,200,200),[20,screenHeight-45,120,40])
    screen.blit(addText , (20,screenHeight-45))

    # Predator Button
    pygame.draw.rect(screen,(200,200,200),[150,screenHeight-45,190,40])
    screen.blit(predText , (150,screenHeight-45))

    # Other Text
    screen.blit(counterText , (20,20))
    screen.blit(DorNText , (40,20))


    for i in range(len(young)):
        screen.blit(youngPlayerImage, ((int(young[i].x)), (int(young[i].y))))
        if young[i].sleep == True and young[i].sleepCounter < 2:
            young[i].sleepCounter +=1
        else:
            young[i].randomCordClass(int(young[i].x), int(young[i].y), int(young[i].speed))
            young[i].sleep = False
            young[i].sleepCounter = 4
        # Young Counters
        young[i].counter +=1

    for i in range(len(adult)):
        screen.blit(adultPlayerImage, ((int(adult[i].x)), (int(adult[i].y))))
        if adult[i].sleep == True and adult[i].sleepCounter < 2:
            adult[i].sleepCounter +=1
        else:
            adult[i].randomCordClass(int(adult[i].x), int(adult[i].y), int(adult[i].speed))
            adult[i].sleep = False
            adult[i].sleepCounter = 4
        # Adult Counters
        adult[i].counter +=1

    for i in range(len(elderly)):
        screen.blit(elderlyPlayerImage, ((int(elderly[i].x)), (int(elderly[i].y))))
        if elderly[i].sleep == True and elderly[i].sleepCounter < 2:
            elderly[i].sleepCounter +=1
        else:
            elderly[i].randomCordClass(int(elderly[i].x), int(elderly[i].y), int(elderly[i].speed))
            elderly[i].sleep = False
            elderly[i].sleepCounter = 4
        # Elderly Counters
        elderly[i].counter +=1

    for i in range(len(predator)):
        screen.blit(predatorImage, ((int(predator[i].x)), (int(predator[i].y))))
        predator[i].randomCordClass(int(predator[i].x), int(predator[i].y))

        # Predator Counters
        predator[i].counter +=1

        # Predator Kill
        predKill(young, youngRemove)
        predKill(adult, adultRemove)
        predKill(elderly, elderlyRemove)


    for i in young:
        if i.counter > 5 and len(young) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                young.remove(i)
                cat = AdultCat(i.x,i.y,i.speed,i.jump,i.attitude,0,4, False)
                adult.append(cat)
    
    for i in adult:
        if i.counter > 5 and len(adult) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                adult.remove(i)
                cat = ElderlyCat(i.x,i.y,i.speed,i.jump,i.attitude,i.counter,4, False)
                elderly.append(cat)

    for i in elderly:
        if i.counter > 15 and len(elderly) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                elderly.remove(i)
    
    for i in predator:
        if i.counter >= 10:
            predator.remove(i)

    for i in youngRemove:
        try:
            young.remove(i)
        except ValueError as error:
            print("Not in list")
        youngRemove.remove(i)

    for i in adultRemove:
        try:
            adult.remove(i)
        except ValueError as error:
            print("Not in list")
        adultRemove.remove(i)

    for i in elderlyRemove:
        try:
            elderly.remove(i)
        except ValueError as error:
            print("Not in list")
        elderlyRemove.remove(i)

    pygame.time.wait(800)
    pygame.display.update()
    