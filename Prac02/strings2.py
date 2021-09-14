#
# strings2.py - read in a string, turn to upper case and duplicate, and print every second character and print every second character minus first and last characters
#

instring = input("Enter a string: ")
# *** add upper and duplicating code here
instring = instring.upper() + instring.upper()


# ///////////// test /////////////

print("Doubled string : ", instring, "\n")



# ///////////// second characters with a while loop /////////////

counter = 1
print("Every Second Character is : ", end="")
while len(instring) > counter:
    print(instring[(counter)], end="")
    counter = counter + 2
print()

# minus first and last
counter = 1
print("Every Second Character minus first and last is : ", end="")
while (len(instring)-2) > counter:
    print(instring[(counter)], end="")
    counter = counter + 2
print("\n")



# ///////////// second characters with a range loop /////////////

print("Every Second Character is : ", end="")
for index in range (1, len(instring), 2):
    print(instring[(index)], end="")
print()

# minus first and last
print("Every Second Character minus first and last is : ", end="")
for index in range (1, (len(instring)-2), 2):
    print(instring[(index)], end="")
print("\n")



# ///////////// second characters with slicing /////////////

print('Every Second Character is :', instring[1::2])

# minus first and last
modInstring = instring[1:-1]
print('Every Second Character minus first and last is :', modInstring[::2])


