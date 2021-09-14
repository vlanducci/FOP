#
# playingCards.py - selecting random biscuits from a pack
#

import random

cards = ["Ace, Spades","2, Spades", "3, Spades", "4, Spades", "5, Spades", "6, Spades", "7, Spades", "8, Spades", "9, Spades", "10, Spades", "Jack, Spades", "Queen, Spades", "King, Spades",  "Ace, Hearts","2, Hearts","3, Hearts","4, Hearts","5, Hearts","6, Hearts","7, Hearts","8, Hearts","9, Hearts","10, Hearts","Jack, Hearts","Queen, Hearts","King, Hearts", "Ace, Diamonds","2, Diamonds","3, Diamonds","4, Diamonds","5, Diamonds","6, Diamonds","7, Diamonds","8, Diamonds","9, Diamonds","10, Diamonds","Jack, Diamonds","Queen, Diamonds","King, Diamonds", "Ace, Clubs","2, Clubs","3, Clubs","4, Clubs","5, Clubs","6, Clubs","7, Clubs","8, Clubs","9, Clubs","10, Clubs","Jack, Clubs","Queen, Clubs","King, Clubs",]

print('\nCARD DECK\n')

print('There are ', len(cards), ' cards in the deck.')

print('\n', cards, '\n')

more = input('\nWould you like 5 cards (Y/N)?: ')
more = more.upper()

while more != "N":
    if len(cards) == 0:
        print("\nSorry, no more cards left :(")
        break
    else:
        for i in range(1,6):
            choice = random.randint(0,len(cards)-1)
            print("- Card", i, "is:", cards[choice])
            del cards[choice]
        more = input("\n\nWould you like 5 more cards (Y/N)?: ")
        more = more.upper()

print('\nThere are ', len(cards), ' cards left.')
print('\n', cards, '\n')

