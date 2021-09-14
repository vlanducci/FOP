#
# converter.py - convert between our temperature formats
#

import conversions as cv

loop = "Y"

print("\n-----------WELCOME TO CONVERSIONS-----------\n\n")

while loop == "Y":

    choice = input("\nWould you like to convert another tempreture? (Y)es, (N)o, (I)nfo: ")
    choice = choice.upper()

    if choice == "Y":
        tempType = float(input("\nWhat type of conversion? (1-6): "))
        if tempType == 1:
            temp = float(input("\nEnter tempreture: "))
            newTemp = cv.fahr2cel(temp)
        elif tempType == 2:
            temp = float(input("\nEnter tempreture: "))
            newTemp = cv.cel2fahr(temp)
        elif tempType == 3:
            temp = float(input("\nEnter tempreture: "))
            newTemp = cv.kel2fahr(temp)
        elif tempType == 4:
            temp = float(input("\nEnter tempreture: "))
            newTemp = cv.fahr2kel(temp)
        elif tempType == 5:
            temp = float(input("\nEnter tempreture: "))
            newTemp = cv.cel2kel(temp)
        elif tempType == 6:
            temp = float(input("\nEnter tempreture: "))
            newTemp = cv.kel2cel(temp)
        print("New tempreture is", newTemp)

    elif choice == "N":
        loop = "N"

    elif choice == "I":
        print(" - fahr2cel : Convert from Fahrenheit to Celsius.\n - cel2fahr : Convert from Celsius to Fahrenheit.\n - kel2fahr : Convert from Kelvin to Fahrenheit.\n - fahr2kel : Convert from Fahrenheit to Kelvin.\n - cel2kel  : Convert from Celsius to Kelvin.\n - kel2cel  : Convert from Kelvin to Celsius. ")

    else:
        print("ERROR - unknown input")

print("\nGoodbye\n")


