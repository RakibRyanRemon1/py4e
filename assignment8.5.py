file_name = input("Enter file name: ")
file_handle = open(file_name)
count = 0
for line in file_handle:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1:
        continue
    if words[0] == '':
        continue
    if words[0] != 'From':
        continue
    count += 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")

