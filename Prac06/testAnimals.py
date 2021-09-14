#
# testAnimals.py - test animals classes and somewhat implements them
#

from animals import Cat
from animals import Dog
from animals import Bird

garfield = Cat("Garfield", "1/1/1978", "Orange", "Tabby")
garfield.printit()
print(garfield,"\n")

doggo = Dog("Puggsy", "1/1/1978", "Brown", "Pug")
doggo.printit()
print(doggo,"\n")

birdy = Bird("Cracker", "1/1/1978", "Yellow", "birdy?")
birdy.printit()
print(birdy,"\n")
