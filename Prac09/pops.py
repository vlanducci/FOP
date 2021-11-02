
pops = {'New South Wales': 7757843, 'Victoria' : 6100877, 'Queensland' : 4860448, 'South Australia' : 1710804, 'Western Australia' : 2623164,'Tasmania': 519783,'Northern Territory' : 245657,'Australian Capital Territory': 398349}
total = 0

print('\nprint population of each state:')
for k in pops.keys():
  print(pops[k])
  total += pops[k]

print('\nprint total pop:')
print(total)

print('\nprint population of state if under 3000000:')
for k in pops.keys():
  if pops[k] > 3000000:
    print(k, ' : ', pops[k])

print('\nprint states:')
for p in pops:
  print(p)

print('\nprint states with pops:')
for k in pops.keys():
  print(k, ' : ', pops[k])

if 'New Zealand' in pops:
  print('yes')