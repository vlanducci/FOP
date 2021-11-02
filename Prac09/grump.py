import sys

punctuation = '~!@#$%^&*()_+{}|:"<>?`=[]\\;\',./'

if len(sys.argv) <2 :
  filename = 'rumple.txt'
else:
  filename = sys.argv[1]

book = open(filename).read()
bookP = book.translate(str.maketrans('','',punctuation))
words = bookP.lower().split()
print(len(words))
print(words[:10])