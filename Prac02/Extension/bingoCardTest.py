#
# bingoCard.py - generates a bigo card with random numbers (testing different method)
#

import random

numList = list(range(1, 101))

print("\nBINGO CARD\n")

more = input("Do you want to generate a bingo card (Y/N)?: ")
more = more.upper()

while more == "Y":
    cardNums = random.sample(numList, 23)

    print("\n  " + str(cardNums[0]) + "   |   " + str(cardNums[1]) + "   |   " + str(cardNums[2]) + "   |   " + str(cardNums[3]) + "   |   " + str(cardNums[4]) + "   \n-------+-------+-------+-------+------- \n  " + str(cardNums[5]) + "   |   " + str(cardNums[6]) + "   |   " + str(cardNums[7]) + "   |   " + str(cardNums[7]) + "   |   " + str(cardNums[8]) + " \n-------+-------+-------+-------+-------  \n  " + str(cardNums[9]) + "   |   " + str(cardNums[10]) + "   |  free  |   " + str(cardNums[11]) + "   |   " + str(cardNums[12]) + "   \n-------+-------+-------+-------+------- \n  " + str(cardNums[13]) + "   |   " + str(cardNums[14]) + "   |   " + str(cardNums[15]) + "   |   " + str(cardNums[16]) + "   |   " + str(cardNums[17]) + " \n-------+-------+-------+-------+-------  \n  " + str(cardNums[18]) + "   |   " + str(cardNums[19]) + "   |   " + str(cardNums[20]) + "   |   " + str(cardNums[21]) + "   |   " + str(cardNums[22]) + "   \n")
    
    more = input("Do you want to generate a bingo card (Y/N)?: ")
    more = more.upper()


