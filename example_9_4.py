# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
han = open('mbox-short.txt')

counts = dict()
namemax = None
max = None
for line in han:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0]!='From':
        continue
    names = words[1]
    counts[names] = counts.get(names,0)+1

for name,count in counts.items():
    if max is None or max < count:
        namemax = name
        max = count
print(namemax,max)
