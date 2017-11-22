import sys

table = {'а':'a',
	'б':'b',
	'в':'v',
	'г':'g',
	'д':'d',
	'е':'e',
	'ё':'yo',
        'ж':'zh',
	'з':'z',
	'и':'i',
	'й':'y',
	'к':'k',
	'л':'l',
	'м':'m',
	'н':'n',
	'о':'o',
	'п':'p',
	'р':'r',
	'с':'s',
	'т':'t',
	'у':'u',
	'ф':'f',
	'х':'h',
	'ц':'ts',
	'ч':'ch',
	'ш':'sh',
	'щ':'tsch',
	'э':'e',
	'ю':'yu',
	'я':'ya'}

#read through lines in a file
for line in sys.stdin.readlines():
	line = line.strip('\n') #remove newlines
	if line == '':  #if the line is blank (sentence boundary)
		print()
		continue
	if line[0] == '#': # if the line is a comment
		print(line)
		continue

	row = line.split('\t')
	# take the wordform (column 2)
	transliterated = row[1]

	# transliterate it
	for c in table:
		transliterated = transliterated.replace(c, table[c])
	#set the 10th column to the transliterated form
	row[9] = ('Tr=' + transliterated)

	#print out line separated by tabs
	print('\t'.join(row))