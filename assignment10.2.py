# python 3.8
# file input
file_name = input("Enter file: ")
if len(file_name) < 1:
    file_name = 'mbox-short.txt'
file_handler = open(file_name)
# dictionary & word split
word_dict = dict()
for line in file_handler:
    line = line.rstrip()
    words = line.split()
    # fail safe
    if len(words) < 3:
        continue
    # finding email address & adding to dictionary
    if words[0] == 'From':
        temp = words[5]
        temp = temp.split(':')
        temp = temp[0]
        word_dict[temp] = word_dict.get(temp, 0) + 1

tmp = list()

# for key, val in d.items():
t = word_dict.items()
t = sorted(t)
for key, val in t:
    print(key, val)

