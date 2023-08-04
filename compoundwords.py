# permutations, itertools, string processing, input output

import sys
from itertools import permutations

words = []
compound = []

# required because of "read until eof"
for line in sys.stdin:
    line = line.split()

    words.extend(line)        

# brute force all permutations
for (x, y) in permutations(words, 2):
    compound.append(x + y)

# eliminate duplicates
compound = list(set(compound))
compound.sort()

for c in compound:
    print(c)

