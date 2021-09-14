#
# assorted.py - selecting random biscuits from a pack
#

import random

biscuits = []

biscuits.extend(["Monte Carlo"]*1)
biscuits.extend(["Shortbread Cream"]*2)
biscuits.extend(['Delta Cream']*4)
biscuits.extend(['Orange Slice']*2)
biscuits.extend(['Kingston']*2)

print('\nASSORTED CREAMS\n')

print('There are ', len(biscuits), ' biscuits in the pack.')

print('\n', biscuits, '\n')

more = input('\nWould you like a biscuit (Y/N)?: ')

while more != "N":
    if len(biscuits) == 0:
        print("\nSorry, no more biscits left :(\n")
        break
    else:       
        choice = random.randint(0,len(biscuits)-1)
        print("Your biscuit is:", biscuits[choice])
        del biscuits[choice]
        more = input("\nWould you like a biscuit (Y/N)?: ")
        
print('\nThere are ', len(biscuits), ' biscuits left.')
print('\n', biscuits, '\n')

