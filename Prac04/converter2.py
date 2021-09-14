#
# converter.py - convert list between our temperature formats
#

import conversions as cv

loop = "Y"

print("\n-----------WELCOME TO CONVERSIONS-----------\n\n")

while loop == "Y":
    tempList = []
    
    choice = input("\nWould you like to convert another tempreture? (Y)es, (N)o, (I)nfo: ")
    choice = choice.upper()

    if (choice == "N") or (choice == ""):
        loop ="N"

    elif choice == "Y":
        tempType = float(input("\nWhat type of conversion? (1-6): "))
        temp = float(input("\nEnter tempreture: "))
        if tempType == 1:
            newTemp = cv.fahr2cel(temp)
        elif tempType == 2:
            newTemp = cv.cel2fahr(temp)
        elif tempType == 3:
            newTemp = cv.kel2fahr(temp)
        elif tempType == 4:
            newTemp = cv.fahr2kel(temp)
        elif tempType == 5:
            newTemp = cv.cel2kel(temp)
        elif tempType == 6:
            newTemp = cv.kel2cel(temp)
        print("New tempreture is", newTemp)

    elif choice == "I":
        print(" - fahr2cel : Convert from Fahrenheit to Celsius.\n - cel2fahr : Convert from Celsius to Fahrenheit.\n - kel2fahr : Convert from Kelvin to Fahrenheit.\n - fahr2kel : Convert from Fahrenheit to Kelvin.\n - cel2kel  : Convert from Celsius to Kelvin.\n - kel2cel  : Convert from Kelvin to Celsius. ")

    else:
        print("ERROR - unknown input")

print("\nGoodbye\n")


