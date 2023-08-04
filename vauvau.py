# easy, arithmetic, mod

def attack(start, fin, e):
    cyc = start+fin
    
    if e%cyc != 0 and e%cyc <= start:
            return 1
    return 0

def result(val):
    if val == 0:
        print("none")
    elif val == 1:
        print("one")
    else:
        print("both")

(a, b, c, d) = list(map(int, input().split()))
(p, m, g) = list(map(int, input().split()))

result(attack(a, b, p) + attack(c, d, p))
result(attack(a, b, m) + attack(c, d, m))
result(attack(a, b, g) + attack(c, d, g))


