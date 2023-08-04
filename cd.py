# medium, input, readlines, set

from sys import *

lines = stdin.readlines()

m, n = map(int, lines[0].split())

current = 1
while n != 0 and m != 0:
    # it is possible that these must be aggregate operations to avoid timeout
    jack = set(lines[current:current+m])
    current += m
    jill = set(lines[current:current+n])
    current += n
    
    print(len(jack & jill))

    m, n = map(int, lines[current].split())
    current += 1
