import string
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.strip()
    line = line.translate(line.maketrans(' ', ' ', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] +=1
print(counts)

#print(fhand.read())
