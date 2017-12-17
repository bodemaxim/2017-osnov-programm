import re
import io

# Define the names of the files
srt_file = 'Subtitles.srt'
txt_file = 'A2.txt'
out_file = 'New_Subtitles.srt'


# Get asterisks to replace words
def get_stars(word):
    return '*' * len(word)

# Read txt file
with io.open(txt_file, "r", encoding="latin-1") as f:
    # Delete punctuation from the array of words
    read_data = re.sub('\.|,|-|\?|!|:|\d', '', f.read()).split()
    # Delete all duplicated symbols
    unique_words = set(read_data)

f.closed

# Read srt file
with open(srt_file) as f:
    read_data = f.read()
    # Replace equalling words
    for word in unique_words:
        read_data = re.sub(r'\b' + word + r'\b', get_stars(word), read_data, flags=re.I)

f.closed

# Write output to a file
f = open(out_file, 'w+')
f.writelines(read_data)
f.close()
