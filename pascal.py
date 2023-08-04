# discrete math, divisibility, divisors, arithmetic, time limit exceeded

from math import *

# algorithm is about divisibility as presented
# brute force won't work

n = int(input())

first = 0

for i in range(2, ceil(sqrt(n+1))):
    if n%i==0:
        first = i
        break

if first == 0:
    print(n-1)
else:
    print(int(n-(n/first)))

