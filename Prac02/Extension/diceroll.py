#
# diceroll.py - simulate rollinging a dice multiple times
#

import random

dice = ["1", "2", "3", "4", "5", "6"]
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

print ("\nDICE ROLL\n")

trials = int(input("How many rolls?: "))

for index in range(trials):
    if random.choice(dice) == "1":
        one = one + 1
    elif random.choice(dice) == "2":
        two = two + 1
    elif random.choice(dice) == "3":
        three = three + 1
    elif random.choice(dice) == "4":
        four = four + 1
    elif random.choice(dice) == "5":
        five = five + 1
    else:
        six = six + 1

print("\nThere were ", one, " ones, ", two, " twos, ", three, " threes, ", four, " fives, ", six, " and sixes.\n")

