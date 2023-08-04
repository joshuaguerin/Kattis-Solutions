# math, factorial, kamenetsky

from math import *

# The Kamenetsky formula is valid for 1 < n < 6561101970383
def kamenetsky(n):
    return ceil(.5 * (log(2*pi) - 2*n + log(n)*(1 + 2 * n))/log(10) )

import sys

# required because of "read until eof"
for line in sys.stdin:
    n = int(line)
    if n == 0 or n == 1:
        print(1)
    else:
        print(kamenetsky(n))
        
