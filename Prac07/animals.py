#
# animals.py - classes on animals
#

class Cat():
  myclass = "Cat"
  def __init__(self, name, dob, colour, breed):
    self.name = name
    self.dob = dob
    self.colour = colour
    self.breed = breed
  
  def printit(self):
    print('Name: ', self.name)
    print('DOB: ', self.dob)
    print('Colour: ', self.colour)
    print('Breed: ', self.breed)
    print('Class: ', self.myclass)

class Dog():
  myclass = "Dog"
  def __init__(self, name, dob, colour, breed):
    self.name = name
    self.dob = dob
    self.colour = colour
    self.breed = breed
  def printit(self):
    print('Name: ', self.name)
    print('DOB: ', self.dob)
    print('Colour: ', self.colour)
    print('Breed: ', self.breed)
    print('Class: ', self.myclass)

class Bird():
  myclass = "Bird"
  def __init__(self, name, dob, colour, breed):
    self.name = name
    self.dob = dob
    self.colour = colour
    self.breed = breed
  def printit(self):
    print('Name: ', self.name)
    print('DOB: ', self.dob)
    print('Colour: ', self.colour)
    print('Breed: ', self.breed)
    print('Class: ', self.myclass)

class Shelter():
  def __init__(self, name, address, phone):
    self.name = name
    self.address = address
    self.phone = phone
    self.processing = []
    self.available = []
    self.adopted = []

  def displayProcessing(self):
    print('Current processing list:')
    for a in self.processing:
      a.printit()
    print()

  def displayAvailable(self):
    # add your code here  

  def displayAdopted(self):
    # add your code here

  def displayAll(self):
    self.displayProcessing()

  def newAnimal(self, type, name, dob, colour, breed):
    temp = None
    if type == 'Dog':
      temp = Dog(name, dob, colour, breed)
    elif type == 'Cat':
      temp = Cat(name, dob, colour, breed)
    elif type == 'Bird':
      temp = Bird(name, dob, colour, breed)
    else:
      print('Error, unknown animal type: ', type)
    if temp:
      self.processing.append(temp)
      print('Added ', name, ' to processing list')
      self.displayAll()

  def makeAvailable(self, name):
    # add your code here
    
  def makeAdopted(self, name):
    # add your code here
