import pygame, sys
import numpy as np
import random

pygame.init()

players = []
loop = True
screenWidth = 800
screenHeight = 600
playersL = []


screen = pygame.display.set_mode((screenWidth, screenHeight))
playerImage = pygame.image.load("Goose_portrait.png")
playerImage = pygame.transform.scale(playerImage, (50, 50))

# playersNum = int(input("Amount: "))
playersNum = 4  # for testing

for _ in range(playersNum):
    x = random.randint(0,screenWidth)
    y = random.randint(0, screenHeight)
    cords = str(x) + "," + str(y)
    players.append(cords)
for i in players:
    split = i.split(',')
    if ',' in split:
        split = split.remove(',')
    playersL.append(split)

def cordChange():
    for i in players:
        xStep = random.randint(0,10)
        yStep = random.randint(0,10)
        i[0] = str(int(i[0]) + xStep)
        i[1] = str(int(i[1]) + yStep)

def player():
    screen.fill((0,0,0))
    for i in playersL:
        screen.blit(playerImage, ((int(i[0])), (int(i[1]))))
    for i in playersL:
        xStep = random.randint(0,10)
        yStep = random.randint(0,10)
        pOrm = random.randint(0,1)
        if pOrm == 0:
            i[0] = str(int(i[0]) + xStep)
            i[1] = str(int(i[1]) + yStep)
        else:
            i[0] = str(int(i[0]) - xStep)
            i[1] = str(int(i[1]) - yStep) 

while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    

    player()

    pygame.time.wait(100)



    pygame.display.update()

