import re #import regular expressions module
import io #import io module to handle textual data as a stream (a sequence of data elements made available over time)

# Define the names of the files
srt_file = 'Subtitles.srt'
txt_file = 'text.txt'
out_file = 'New_Subtitles.srt'

# Get asterisks for letters in words
def get_stars(word): #create a variable 'get_stars' for it to be a function applied to the variable 'word'
    return '*' * len(word) #define the function as replacing each symbol in a word with asterisks

# Read txt file
with io.open(txt_file, "r", encoding="utf-8") as f: #open txt_file for reading and handle it as a variable 'f'
    # Delete all special character set from array of words
    read_data = re.sub('\.|,|-|\?|!|:|\d', '', f.read()).split() #use regex to delete punctuation, split words by spaces
    # Delete all duplicated symbols
    unique_words = set(read_data) #use set function to draw unique elements from the string 'read_data'

f.closed

# Read srt file
with open(srt_file) as f: #open srt_file and handle it as a variable 'f'
    read_data = f.read()
    # Replace equalling words
    for word in unique_words:
        read_data = re.sub(r'\b' + word + r'\b', #pattern to replace (a word within two boundaries)
		get_stars(word), #asterisks to replace equalling words
		read_data, #data string where changes happen
		flags=re.I) #ignore case when replacing


f.closed

# Write output to file
f = open(out_file, 'w+')
f.writelines(read_data)
f.close()
