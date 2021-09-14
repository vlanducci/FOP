#
# bingoCard.py - generates a bigo card with random numbers
#

import random

y = "Y"
cardNums = []

print("\nBINGO CARD\n")

more = input("Do you want to generate a bingo card (Y/N)?: ")
more = more.upper()

for i in range(0,23):
    while y == "Y":
        num = random.sample(numList,100)
        if num in cardNums:
            y = "Y"
        else:
            cardNums.append(num)
            y = "N"
    y = "Y"

print("\n  " + str(cardNums[0]) + "   |   " + str(cardNums[1]) + "   |   " + str(cardNums[2]) + "   |   " + str(cardNums[3]) + "   |   " + str(cardNums[4]) + "   \n-------+-------+-------+-------+------- \n  " + str(cardNums[5]) + "   |   " + str(cardNums[6]) + "   |   " + str(cardNums[7]) + "   |   " + str(cardNums[7]) + "   |   " + str(cardNums[8]) + " \n-------+-------+-------+-------+-------  \n  " + str(cardNums[9]) + "   |   " + str(cardNums[10]) + "   |  free  |   " + str(cardNums[11]) + "   |   " + str(cardNums[12]) + "   \n-------+-------+-------+-------+------- \n  " + str(cardNums[13]) + "   |   " + str(cardNums[14]) + "   |   " + str(cardNums[15]) + "   |   " + str(cardNums[16]) + "   |   " + str(cardNums[17]) + " \n-------+-------+-------+-------+-------  \n  " + str(cardNums[18]) + "   |   " + str(cardNums[19]) + "   |   " + str(cardNums[20]) + "   |   " + str(cardNums[21]) + "   |   " + str(cardNums[22]) + "   \n")

