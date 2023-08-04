# easy, io, dictionary, map

import sys

translate = {}

# Read/process everything up to the newline
line = input()
while line != "":
    (translation, entry) = line.split()
    
    translate[entry] = translation

    line = input()

# Read/process remaining lines
for word in sys.stdin:
    word = word[:len(word)-1]
    if word in translate:
        print(translate[word])
    else:
        print("eh")
