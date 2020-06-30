# Read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
han = open(name)
count = dict()
lst = list()
for line in han:
    line = line.rstrip()
    words = line.split()
    if len(words) < 7 or words[0]!='From':
        continue
    time = words[5]
    parts = time.split(':')
    hours = parts[0]
    count[hours] = count.get(hours,0)+1
for h,c in count.items():
    lst.append((h,c))
lst = sorted(lst)
for h,c in lst:
    print(h,c)
