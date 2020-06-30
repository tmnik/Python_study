# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below.
fname = input('Enter the name file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
try:
    fh = open(fname)
except:
    print('Error, please enter .txt file')
    quit()
count = 0
all_numb = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count+1
    n = line.find(':')
    numb = line[n+1:]
    numb = float(numb)
    print(numb)
    all_numb = all_numb+numb
sred = all_numb/count
print('Average spam confidence:'+str(sred))
