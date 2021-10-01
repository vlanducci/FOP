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
    speed = random.randint(2,10)
    jump = random.randint(2,10)
    attitude = random.randint(0,1)
    cords = str(x) + "," + str(y)
    cat = YoungCat(x,y,speed,jump,attitude, 0)
    young.append(cat)


while loop:
    population = len(young)+len(adult)+len(elderly)
    counter += 1
    print(population)
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
            x = random.randint(200,screenWidth-200)
            y = random.randint(200, screenHeight-200)
            speed = random.randint(2,10)
            jump = random.randint(2,10)
            attitude = random.randint(0,1)
            cords = str(x) + "," + str(y)
            cat = YoungCat(x,y,speed,jump,attitude, 0)
            young.append(cat)
            
    pygame.draw.rect(screen,(200,200,200),[20,screenHeight-45,120,40])

    screen.blit(addText , (20,screenHeight-45))
    screen.blit(counterText , (20,20))
    
    for i in range(0,len(young)):
        screen.blit(youngPlayerImage, ((int(young[i].x)), (int(young[i].y))))
        young[i].randomCordClass(int(young[i].x), int(young[i].y), int(young[i].speed))
        # print("cat", str(i), young[i].x, young[i].y, young[i].speed)

    for i in range(len(adult)):
        screen.blit(adultPlayerImage, ((int(adult[i].x)), (int(adult[i].y))))
        adult[i].randomCordClass(int(adult[i].x), int(adult[i].y), int(adult[i].speed))
        # print("cat", str(i), young[i].x, young[i].y, young[i].speed)

    for i in range(0,len(elderly)):
        screen.blit(elderlyPlayerImage, ((int(elderly[i].x)), (int(elderly[i].y))))
        elderly[i].randomCordClass(int(elderly[i].x), int(elderly[i].y), int(elderly[i].speed))
        # print("cat", str(i), young[i].x, young[i].y, young[i].speed)


    for i in young:
        if i.counter > 5 and len(young) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                young.remove(i)
                cat = AdultCat(i.x,i.y,i.speed,i.jump,i.attitude,0)
                adult.append(cat)
    
    for i in adult:
        if i.counter > 5 and len(adult) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                adult.remove(i)
                cat = ElderlyCat(i.x,i.y,i.speed,i.jump,i.attitude,i.counter)
                elderly.append(cat)

    for i in elderly:
        if i.counter > 15 and len(elderly) > 0:
            yOrn = random.randint(0,1)
            if yOrn == 0:
                elderly.remove(i)

    for i in range(len(young)):
        young[i].counter +=1
    for i in range(len(adult)):
        adult[i].counter +=1
    for i in range(len(elderly)):
        elderly[i].counter +=1

    pygame.time.wait(800)
    pygame.display.update()
    