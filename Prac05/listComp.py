#
# listComp.py - loops and list comprehensions
#

################ loops ################

numbers = []
for i in range(1,6):
    numbers.append(i)

###

triple_numbers = []
def triple(numbers):
    for n in numbers:
        triple_numbers.append(n * 3)
triple(numbers)
print(triple_numbers)

###

new = []
string = input("Enter string: ")
split = list(string)

for i in split:
    if i.isdigit() == False:
        new.append(i)
        print(i, end="")
print()

###

cap = []
text = input("Enter text: ")
sText = text.split()

for i in sText:
    print(i[0].upper(), end="")
    print(i[1::], end=" ")
print()


################ list comprehensions ################

numbers = [i for i in range(1,6)]
print(numbers)

###

triple_numbers = [n * 3 for n in numbers]
print(triple_numbers)

###

string = input("Enter string: ")
split = list(string)
new = [print(i, end="") for i in split if i.isdigit() == False]
print()

###

text = input("Enter text: ")
sText = text.split()
cap = [print(i[0].upper() + i[1::], end=" ") for i in sText]
#cap = print([sText[i][0].upper(), for i in range(len(sText))])
print()
