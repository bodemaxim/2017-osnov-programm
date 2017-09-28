import sys

#Let's count characters
text = sys.stdin.read()
characters = len(text)
print(characters)

# we suppose that the number of words equals the number of spaces plus one
#let's count spaces first

spaces = 0

for c in sys.stdin.read():
	if c ==' ': #the  space my be extra
		spaces == spaces + 1

#let's count words
words = spaces + 1
print(words)

#let's count new lines, to say it so, 'enters'

enters = 0

for d in sys.stdin.read():
	if d =='\n': #the \n may be extra
		enters == enters + 1

#let's count lines
lines = enters + 1
print(lines)


