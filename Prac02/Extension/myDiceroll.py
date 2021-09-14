#
# myDiceroll.py - simulate rollinging a dice multiple times (my version)
#

import random
import os

print ("\nDICE ROLL\n")

run = input("Roll the dice? (Y)es, (N)o: ")
run = run.upper()

while run == "Y":
    os.system("clear")
    dice = random.randint(1,6)
    print("\nResult:", dice, end="\n")
    run = input("\nRoll the dice again? (Y)es, (N)o: ")
    run = run.upper()

print("\nGoodbye!\n")
