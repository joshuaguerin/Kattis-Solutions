# Catalan numbers, binomial coefficient, math

from math import factorial

# standard def. of binomial coefficient
def binom(n, k):
    # speed-up according to CP3 (not needed)
    # if k > n-k:
    #     k = n - k

    # make sure results are big ints, not decimal (overflowerror)
    return factorial(n) // (factorial(n-k) * factorial(k))

# closed form for the nth Catalan number from CP3
def catalan(n):
    # make sure results are big ints, not decimal (overflowerror)
    return binom(2*n, n) // (n+1)

q = int(input())

for i in range(q):
    x = int(input())
    print(catalan(x))
