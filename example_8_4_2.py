# Open the file and read it line by line.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
fname = input('Enter the name file: ')
if len(fname) < 1 : fname = 'romeo.txt'
try:
    fh = open(fname)
except:
    print('Error, please enter .txt file')
    quit()
words = list()
for line in fh:
    line = line.rstrip()
    part = line.split()
    for word in part:
        if words == []:
            words.append(word)
        if word not in words:
            words.append(word)
words.sort()
print(words)
