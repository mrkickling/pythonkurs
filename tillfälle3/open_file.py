f = open("fil.txt")

for line in f.readlines():
    for word in line.split():
        print(word)
