#
# Student Name: Viola Landucci
# Student ID : 20769446
#
# test1.py: Create a string and print it
#

brianlist = ["Bright", "Side", "of", "Life", "<whistle>"] 

print("\nPrac Test 1 Words:\n")

for i in range(len(brianlist)):
    if (i % 2) == 0:
        word = brianlist[i]
        word = word[::-1].lower()
        word = word[::3]
    else:
        word = brianlist[i].upper()
    print(i, word)

