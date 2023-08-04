from math import pi

r, c = input().split()
r = int(r)
c = int(c)

a_cheese = pi * (r-c)**2
a_total = pi * r**2

print((a_cheese/a_total) * 100)

