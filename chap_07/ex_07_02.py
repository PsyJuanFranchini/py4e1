# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
print("Done")
