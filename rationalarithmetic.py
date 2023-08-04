from fractions import Fraction

n = int(input())

for i in range(n):
    (n1, d1, op, n2, d2) = input().split()
    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)

    fst = Fraction(n1, d1)
    snd = Fraction(n2, d2)

    if op == '+':
        result = fst + snd
    elif op == '-':
        result = fst - snd
    elif op == '*':
        result = fst * snd
    else:
        result = fst/snd


    num = result.numerator
    denom = result.denominator
    
    print(num, '/', denom)
    
