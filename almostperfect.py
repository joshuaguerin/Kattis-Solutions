# math, discrete, divisors, perfect numbers

import sys
from math import sqrt

def div_sum(n):
    sum_d = 1
    root = sqrt(n)
    i = 2
    
    while i < root:
        if n%i == 0:
            # sum both the index, and n/i
            # ^ reduce search space
            sum_d += i + (n/i)
        i += 1
    # perfect square is a special case
    if n == int(root)**2:
        sum_d += root
    return sum_d

    
# required because of "read until eof"
for n in sys.stdin:
    n = int(n)
    
    sum_divisors = div_sum(n)
    
    if sum_divisors == n:
        print(n, "perfect")
    elif n-2 <= sum_divisors and sum_divisors <= n+2:
        print(n, "almost perfect")
    else:
        print(n, "not perfect")

