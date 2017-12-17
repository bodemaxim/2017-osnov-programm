import sys

m={}
tagfreq={}
wordfreq={}
total=0

#read through each of the lines
for line in sys.stdin.readlines():
	#if the line is a comment, skip it
	if line[0]=='#':
		continue
	#if the line doesn't contain a tab, skip it
	if '\t' not in line:
		continue

#make a list of columns
row=line.split('\t')

tag=row[3]
form=row[1]

if form not in m: #if we haven't seen the form before
	m[form]={} #make a new map to hold tag-> frequency
if tag not in m[form]: #if we haven't seen the tag for this form before
	m[form][tag]=0

if tag not in tagfreq:
	tagfreq[tag]=0
	tagfreq[tag]=tagfreq[tag]+1
if form not in wordfreq:
	wordfreq[form]=0
	wordfreq[form]=wordfreq[form]+1

m[form][tag]=m[form][tag]+1 #increment the count by 1
total=total+1
for tag in tagfreq:
	print(tagfreq[tag]/total,'\t',tagfreq[tag],'\t',tag,'_')
for x in m:
for y in m[x]:
	print(m[x][y]/wordfreq[x],'\t',m[x][y],'\t',y,'\t',x)