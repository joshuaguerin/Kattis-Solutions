# easy, numeric, number theory, discrete math, loops

from math import ceil

s = int(input())

# First line of output
print(s, ':', sep='')

# 2 is the lowest possible starting point
for x in range(2, s):
    # only two values to check per number
    for y in range(x-1, x+1):
        # two possibilities: even number of rows or odd (one extra)
        if s%(x+y) == 0 or s%(x+y)-x == 0:
            print(x, ',', y, sep='')

