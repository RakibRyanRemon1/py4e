# Use the file name mbox-short.txt as the file name
file_name = input("Enter file name: ")
fh = open(file_name)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find('0')
    total += float(line[pos:pos + 6])
    count += 1
average = total / count
print("Average spam confidence:", average)
