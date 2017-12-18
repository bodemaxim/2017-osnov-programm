import sys

wt_dict = {} # a dictinary for word-tag mapping
tagmaxfreq = {} # a dictionary to find the most frequent tag
tmf_list = [] # a list to reverse and find the most freq tag

# Open a sample to find out the tag with max frequency
x = open (sys.argv[1])
sample = x.readlines()
x.close()

for line in sample:
	# if there is no tab char, skip the line
	if '\t' not in line:
		continue
	# if the line is a comment, skip it
	if line [0] == '#':
		continue
	# make a list of cells in the row
	row = line.split('\t')
	# if there are not 4 cells, skip the line
	if len(row) != 4:
		continue
	# the form is the value of the last cell
	form = row[3]
	form = form.strip('\n') 
	# the tag is the value of the 3rd cell
	tag = row[2]
	tag = tag.strip('\n')
	# how frequent
	n = row[1]
	# how probable
	p = row [0]
	p = float (p) # convert a string into a numeral

	# check all forms in train.py and make a new dictionary
	if form != '-':
		tp_counter = 0
		# if we have not seen form yet in out word-tag dictionary		
		if form not in wt_dict:
			wt_dict[form] = tag
			tp_counter = p
		else:
			if p >= tp_counter:
				wt_dict [form] = tag
			else:
				continue

# tag with max frequency
for t in tagmaxfreq:
	tmf_list.append ((int(tagmaxfreq[t]), t))
tmf_list.sort(reverse = True)	
tmf = tmf_list[0][1]

# read the input
doc = sys.stdin.readlines()

for line in doc:
	if '\t' in line:
		row = line.split('\t')
		if len(row) != 10:
			continue
		if '#' in row[0]:
			sys.stdout.write(line)
		else:	
			if row[3] != '-':
				sys.stdout.write(line)
			else:
				n = row [0]
				w = row[1]
				t = row [3]
				translit = row [9]
				newt = '!'
			
				if w in wt_dict:
					newt = wt_dict[w]
				else:
					newt = tmf

				tagged_line = n+'\t'+ w +'\t'+ '-'+'\t'+newt+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+'-'+'\t'+translit
				sys.stdout.write (tagged_line)
	
	else:
		sys.stdout.write (line)


