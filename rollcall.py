# string processing, simple, hash, dictionary, data structures, sorting

import sys

# count first names
firsts = {}
# last, first ordered pairs
names = []

# Create name database
for line in sys.stdin:
        (first, last) = line.split()
        if first in firsts:
                firsts[first] += 1
        else:
                firsts[first] = 1
        names.append((last, first))

# Order database
names.sort()

# Print ordered database
for (last, first) in names:
        if firsts[first] > 1:
                print(first, last)
        else:
                print(first)

