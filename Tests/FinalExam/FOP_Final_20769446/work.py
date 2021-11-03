import sys
import matplotlib.pyplot as plt

def getListK(dict):
  return dict.keys()
def getListV(dict):
  return dict.values()

punctuation = '~!@#$%^&*()_+{}|:"<>?`=[]\\;\',./'
lCounter = 0
uCounter = 0
mCounter = 0
bCounter = 0
eCounter = 0
rCounter = 0
words = []

filename = 'data/scripts/lumberjack.txt'       # supplied in zip file
book = open(filename).read()
bookP = book.translate(str.maketrans('','',punctuation))
split = bookP.lower().split()

for i in split:
  letter = (i.lower())[0]
  
  if "l" in letter:
    lCounter += 1
    words.append(i)
  if "u" in letter:
    uCounter += 1
    words.append(i)
  if "m" in letter:
    mCounter += 1
    words.append(i)
  if "b" in letter:
    bCounter += 1
    words.append(i)
  if "e" in letter:
    eCounter += 1
    words.append(i)
  if "r" in letter:
    rCounter += 1
    words.append(i)

total = lCounter + uCounter + mCounter + bCounter + eCounter + rCounter
print("\nTotal words that start with specified letters:\n" + str(total))


word_counter = {}
for word in words:
  if word in word_counter:
    word_counter[word] += 1
  else:
    word_counter[word] = 1

popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
print("\nMost common to least that included specified letters:")
print(popular_words)

plt.boxplot(getListK(word_counter),getListV(word_counter))
plt.show