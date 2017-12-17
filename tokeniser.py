import sys

sent_id = 1

#for each of the lines in the input
for line in sys.stdin.readlines():
	line = line.strip('\n')
	#skip blank lines
	if line != '':
		newline = ''
		punct = ['.', ',', '(', ')', ':',  '!', '?']
		for x in line:
			if x in punct:
				newline = newline + ' ' + x + ' '
			else:
				newline = newline + x
		#split the line into tokens
		row = newline.split(' ')
		token_id = 1
		#for each of the tokens in the line
		print('# sent_id - %d' % (sent_id))
		print('# text - %s' %(line))
		for token in row:
			if token != '':
				#print out the token with its id
				print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' %(token_id, token))
				token_id = token_id + 1
		print()
		sent_id = sent_id + 1
