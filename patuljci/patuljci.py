# easy, itertools, combinations, brute force

from itertools import *

dwarves = []

for i in range(9):
    dwarves.append(int(input()))

combs = combinations(dwarves, 7)

current = next(combs)
while sum(current) != 100:
    current = next(combs)

for c in current:
    print(c)
