from typing import Counter
import pygame, sys
import numpy as np
import random
from pygame.constants import SRCCOLORKEY
from classes import *
pygame.init()
import math


# ----- Defining Variables ------
loop = True
loop1 = True
deaths = []
young = []
adult = []
elderly = []
cat = []
predator = []
youngRemove = []
adultRemove = []
elderlyRemove = []
totalFoodx = []
totalFoody = []
food = []
counter = 0
population = 0
day = 1
days = 1
youngCap = 0
killed = 0
screenWidth = 800
screenHeight = 600
closenessRange = 20
birthCounter = 0
DARK = (53, 80, 112)
DARKLIGHT = (146, 182, 177)
DorN = ""  # day or night
LorD = ""  # light or dark


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

def eatFood(list):
    for e in range(len(list)):
        clossest = (0,0)
        for i in range(len(food)): 
            if math.sqrt(clossest[0]**2 + clossest[1]**2) < math.sqrt(int(food[i].x)**2 + int(food[i].y)**2): clossest = (int(food[i].x),int(food[i].y))
        if list[e].hungry == True:
            if ((int(list[e].x) - clossest[0] < 20 and (int(list[e].x) - clossest[0] > 0) or ((clossest[0] - int(list[e].x) < 20) and clossest[0] - int(list[e].x) > 0))) and (int(list[e].y) - clossest[1] < 20 and (int(list[e].y) - clossest[0] > 0) or ((clossest[1] - int(list[e].y) < 20) and (clossest[1] - int(list[e].y) > 0))):
                list[e].hungry = False
                list[e].hungryCounter = 3
            else:
                if abs((int(clossest[1])-int(list[e].y))) != 0: 
                    try:
                        list[e].x = int(list[e].x) + ((int(clossest[0])-int(list[e].x))/abs((int(clossest[0])-int(list[e].x))))*int(list[e].speed)                 
                    except ZeroDivisionError as err:
                        None

                if abs((int(clossest[0])-int(list[e].x))) != 0:
                    try:
                        list[e].y = int(list[e].y) + ((int(clossest[1])-int(list[e].y))/abs((int(clossest[1])-int(list[e].y))))*int(list[e].speed)
                    except ZeroDivisionError as err:
                        None


def newCats(randCoord, xCoord, yCoord):
    speed = random.randint(2,3)
    hungry = random.randint(0,1)
    attitude = random.randint(0,1)
    hungry = True if hungry == 0 else False
    if randCoord == "yes":
        x = random.randint(30,729)
        y = random.randint(160, 500)
        cat = YoungCat(x,y,speed,attitude, 0, 4, False, hungry, 3, 0)
    else:
        cat = YoungCat(xCoord,yCoord,speed,attitude, 0, 4, False, hungry, 3, 0)
    young.append(cat) 

def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(20, 770, blockSize):
        for y in range(150, 540, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, LorD, rect, 1)


# Images and Character Icon Settings
screen = pygame.display.set_mode((screenWidth, screenHeight))
youngPlayerImage = pygame.image.load("Images/YoungCat.PNG")
youngPlayerImage = pygame.transform.scale(youngPlayerImage, (30, 30))
adultPlayerImage = pygame.image.load("Images/AdultCat.PNG")
adultPlayerImage = pygame.transform.scale(adultPlayerImage, (30, 30))
elderlyPlayerImage = pygame.image.load("Images/ElderlyCat.PNG")
elderlyPlayerImage = pygame.transform.scale(elderlyPlayerImage, (30, 30))
predatorImage = pygame.image.load("Images/PredatorImage.PNG")
predatorImage = pygame.transform.scale(predatorImage, (30, 30))


# Buttons Settings
smallfont = pygame.font.SysFont('Corbel',35)

# playersNum = int(input("Amount: "))
playersNum = 4  # for testing

for _ in range(playersNum):
    newCats("yes", 0, 0)

for i in range(4):
    x = random.randint(30,729)
    y = random.randint(160, 500)
    newFood = Food(x,y)
    food.append(newFood)



# Start of Program
while loop1:
    screen.fill((DARK))
    pygame.draw.rect(screen,(DARKLIGHT),[screenWidth/2/2+110,screenHeight/2,120,40])

    titleText = smallfont.render("CAT SIMULATION" , True , (DARKLIGHT))
    continueText = smallfont.render("START" , True , (DARK))
    screen.blit(titleText , (screenWidth/2/2+50,screenHeight/2-60))
    screen.blit(continueText , (screenWidth/2/2+120,screenHeight/2+5))

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop1 = False
            loop = False
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and screenWidth/2/2+120 <= mouse[0] <= screenWidth/2/2+120 + 140
            and screenHeight/2+5 <= mouse[1] <= screenHeight/2+5 + 40
        ):
            loop1 = False
    pygame.display.update()


while loop:
    # Counter, Population and Day Counter and determiner 
    population = len(young)+len(adult)+len(elderly)
    counter += 1
    day += 1

    if day > 11:
        day = 0
        days+=1
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
        DARK = (53, 80, 112)
        DARKLIGHT = (146, 182, 177)
    else:
        DARKLIGHT = (243, 217, 221)
        DARK = (199, 130, 131)

    # Buttons Screen Interaction
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and 20 <= mouse[0] <= 20 + 140
            and screenHeight - 45 <= mouse[1] <= screenHeight - 45 + 40
        ):
            newCats("yes",0,0)
        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and 150 <= mouse[0] <= 150 + 140
            and screenHeight - 45 <= mouse[1] <= screenHeight - 45 + 40
        ):
            x = random.randint(200,screenWidth-200)
            y = random.randint(200, screenHeight-200)
            pred = Predator(x,y,0)
            predator.append(pred) 

    # Setting Up Screen
    screen.fill((DARK))
    daysText = "Day: " + str(days)
    counterText = smallfont.render(daysText , True , (DARKLIGHT))
    DorNText = smallfont.render(DorN , True , (DARKLIGHT))
    # pygame.draw.rect(screen, (255,255,255), pygame.Rect(20,150,750,400), 2)
    LorD = (DARKLIGHT)

    # Button
    addText = smallfont.render('Add Cat' , True , (DARK))
    predText = smallfont.render('Add Predator' , True , (DARK))

    # Button Display
    pygame.draw.rect(screen,(DARKLIGHT),[20,screenHeight-45,120,40])
    screen.blit(addText , (20,screenHeight-45))

    # Predator Button
    pygame.draw.rect(screen,(DARKLIGHT),[150,screenHeight-45,190,40])
    screen.blit(predText , (150,screenHeight-45))

    # Other Text and Displays
    screen.blit(counterText , (20,20))
    screen.blit(DorNText , (200,20))
    drawGrid()
    pygame.draw.circle(screen,(84, 95, 102),[200,250], 60)

    for i in range(len(food)):
        pygame.draw.circle(screen,(142, 208, 129),[food[i].x,food[i].y], 10)


    for i in range(len(young)):
        screen.blit(youngPlayerImage, ((int(young[i].x)), (int(young[i].y))))
        if young[i].hungryCounter == 0:
            young[i].hungry = True
        else:
            young[i].hungry = False
        if young[i].sleep == True and young[i].sleepCounter < 2:
            young[i].sleepCounter +=1
        else:
            if young[i].hungry == True:
                eatFood(young)
            else:
                young[i].randomCordClass(int(young[i].x), int(young[i].y), int(young[i].speed))
                young[i].sleep = False
                young[i].sleepCounter = 4
        # moves slower on hill
        originalSpeed = young[i].speed
        if (((int(young[i].x) - 200 < 60 and (int(young[i].x) - 200) > 0) or ((200 - int(young[i].x) < 60) and (200 - int(young[i].x) > 0))) and (int(young[i].y) - 250 < 60 and (int(young[i].y) - 200 > 0) or ((250 - int(young[i].y) < 20) and 250 - int(young[i].y) > 0))):
            young[i].speed = str(1)
        else:
            young[i].speed = originalSpeed

        # Young Counters
        young[i].counter +=1
        if young[i].hungryCounter > 0:
            young[i].hungryCounter -= 1

    for i in young:
        if i.counter > 5 and len(young) > 0:
            yOrn = random.randint(0,1)
            hungry = random.randint(0,1)
            hungry = True if hungry == 0 else False
            if yOrn == 0:
                young.remove(i)
                cat = AdultCat(i.x,i.y,i.speed,i.attitude,0,4, False, hungry, 3, i.hungryCounter)
                adult.append(cat)


    for i in range(len(adult)):
        screen.blit(adultPlayerImage, ((int(adult[i].x)), (int(adult[i].y))))
        if adult[i].hungryCounter == 0:
            adult[i].hungry = True
        else:
            adult[i].hungry = False
        if adult[i].sleep == True and adult[i].sleepCounter < 2:
            adult[i].sleepCounter +=1
        else:
            if adult[i].hungry == True:
                eatFood(adult)
            else:
                adult[i].randomCordClass(int(adult[i].x), int(adult[i].y), int(adult[i].speed))
                adult[i].sleep = False
                adult[i].sleepCounter = 4
        # moves slower on hill
        originalSpeed = adult[i].speed
        if (((int(adult[i].x) - 200 < 60 and (int(adult[i].x) - 200) > 0) or ((200 - int(adult[i].x) < 60) and (200 - int(adult[i].x) > 0))) and (int(adult[i].y) - 250 < 60 and (int(adult[i].y) - 200 > 0) or ((250 - int(adult[i].y) < 20) and 250 - int(adult[i].y) > 0))):
            adult[i].speed = str(1)
        else:
            adult[i].speed = originalSpeed
        
        if i+1 < len(adult):
            oldx = int(adult[i].x)
            newx = int(adult[i+1].x)
            oldy = int(adult[i].y)
            newy = int(adult[i+1].y)
            if ((oldx - newx < closenessRange and oldx - newx > 0) or (oldy - newy < closenessRange) and (oldy - newy < 0)) and (oldy - newy < closenessRange and oldy - newy > 0) or ((newy - oldy < closenessRange) and (newy - oldy > 0)) and adult[i].birthCounter == 0 and adult[i+1].birthCounter == 0:
                if birthCounter == 0:
                    newCats("no", oldx, oldy)
                    print("new cat")
                    adult[i].birthCounter = 4
                    adult[i+1].birthCounter = 4

        # Adult Counters
        adult[i].counter +=1
        if adult[i].hungryCounter > 0:
            adult[i].hungryCounter -= 1
        if adult[i].birthCounter > 0:
            birthCounter -= 1

    for i in adult:
        if i.counter > 5 and len(adult) > 0:
            yOrn = random.randint(0,1)
            hungry = random.randint(0,1)
            hungry = True if hungry == 0 else False
            if yOrn == 0:
                adult.remove(i)
                cat = ElderlyCat(i.x,i.y,i.speed,i.attitude,i.counter,4, False,hungry, 3, i.hungryCounter)
                elderly.append(cat)


    for i in range(len(elderly)):
        screen.blit(elderlyPlayerImage, ((int(elderly[i].x)), (int(elderly[i].y))))
        if elderly[i].hungryCounter == 0:
            elderly[i].hungry = True
        else:
            elderly[i].hungry = False
        if elderly[i].sleep == True and elderly[i].sleepCounter < 2:
            elderly[i].sleepCounter +=1
        else:
            if elderly[i].hungry == True:
                eatFood(elderly)
            else:
                elderly[i].randomCordClass(int(elderly[i].x), int(elderly[i].y), int(elderly[i].speed))
                elderly[i].sleep = False
                elderly[i].sleepCounter = 4
        # moves slower on hill
        originalSpeed = elderly[i].speed
        if (((int(elderly[i].x) - 200 < 60 and (int(elderly[i].x) - 200) > 0) or ((200 - int(elderly[i].x) < 60) and (200 - int(elderly[i].x) > 0))) and (int(elderly[i].y) - 250 < 60 and (int(elderly[i].y) - 200 > 0) or ((250 - int(elderly[i].y) < 20) and 250 - int(elderly[i].y) > 0))):
            elderly[i].speed = str(1)
        else:
            elderly[i].speed = originalSpeed

        # Elderly Counters
        elderly[i].counter +=1
        if elderly[i].hungryCounter > 0:
            elderly[i].hungryCounter -= 1

    for i in elderly:
        if i.counter > 15 and len(elderly) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                elderly.remove(i)


    for i in range(len(predator)):
        screen.blit(predatorImage, ((int(predator[i].x)), (int(predator[i].y))))
        predator[i].randomCordClass(int(predator[i].x), int(predator[i].y))

        # Predator Counters
        predator[i].counter +=1

        # Predator Kill
        predKill(young, youngRemove)
        predKill(adult, adultRemove)
        predKill(elderly, elderlyRemove)
    
    for i in predator:
        if i.counter >= 3:
            predator.remove(i)


    # Error Preventing 
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

    pygame.time.wait(700)
    time = pygame.time.get_ticks()
    pygame.display.update()
    