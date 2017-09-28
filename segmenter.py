import sys

#read in the data
text = sys.stdin.read()

#split the text into sentences
text = text.replace('.','\n')
text = text.replace('!','\n')
text = text.replace('?','\n')

#print part of the text for checking
print(text [1:1000])