from math import factorial as f
import sys

for line in sys.stdin:
    dups = {}
    
    line = line.strip()
    for c in line:
        if c in dups:
            dups[c] += 1
        else:
            dups[c] = 1

    # all permutations (including duplicates)
    perms = f(len(line))

    # If there are v instances of k, assume for a moment that
    # they are distinct.  There are v! permutations of those v copies
    # of the letter k.
    # We must divide out the v! occurrences because they represent
    # the number of times we counted duplicates in our original figure.

    # Do so for all letters
    for k, v in dups.items():
        perms = perms // f(v)
    
    print(perms)
    
