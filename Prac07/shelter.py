#
# shelter.py - uses classes to assign animals
#

from animals import Dog, Cat, Bird, Shelter, Animal

print('\n#### Pet shelter program ####\n')

rspca = Shelter('RSPCA', 'Serpentine Meander', '123456')
rspca.newAnimal('Dog', 'Dude', '1/1/2011', 'Brown', 'Jack Russell')
rspca.newAnimal('Dog', 'Brutus', '1/1/1982', 'Brown', 'Rhodesian Ridgeback')
rspca.newAnimal('Cat', 'Oogie', '1/1/2006', 'Grey', 'Fluffy')
rspca.newAnimal('Bird', 'Big Bird', '10/11/1969', 'Yellow', 'Canary')
rspca.newAnimal('Bird', 'Dead Parrot', '1/1/2011', 'Dead', 'Parrot')

print('\nAnimals added\n')

print('Listing animals for processing...\n')

rspca.displayProcessing()

# This code is commented out until you have implemented
# the methods in animal.py

print('Processing animals...\n')

rspca.makeAvailable('Dude')
rspca.makeAvailable('Oogie')
rspca.makeAvailable('Big Bird')
rspca.makeAdopted('Oogie')

print('\nPrinting updated list...\n')

rspca.displayAll()
rspca.displayAvailable()
rspca.displayAdopted()

