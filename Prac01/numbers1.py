#
# numbers1.py: Read in number and echo the number and its type to screen:
#

numberstr = input("Enter a number: ")
print("Number =", numberstr, " Type: ", str(type(numberstr)))

number = int(numberstr)
print("Number =", number, " Type : ", str(type(number)))

floatNum = float(numberstr)
print("Number =", number, " Type : ", str(type(floatNum)))

