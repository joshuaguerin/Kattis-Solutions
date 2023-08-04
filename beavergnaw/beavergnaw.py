
# |       |
# |       |
# |_______|    _
# \       /    |
#  \_____/     |
#   _|_|_  I d | D 
#  /  d  \     |
# /_______\    -
# |       |
# |   D   |
# ---------

# Cylinder volume: V = pi * r^2 * h
# Tapered cylinder volume: V = 1/3 * pi * h * (R^2 + Rr + r^2)
# where:
#     r
#     ___
#    / | \  | h
#   /__|__\ |
#     R

# for convenience: R = D/2, r = d/2

# So:
# Outer cylinder: Vo = 2*pi*R**3 (pi * R**2 * 2R)
# Inner cylinder: Vi = 2*pi*r**3
# 2 Inner tapered cylinders:
# 2Vt = 2/3 * pi * (R - r)(R**2 + Rr + r**2)
#     = 2/3 * pi * (R**3 - r**3)
# So:
# V = Vo - Vi - 2V2
# Reduce given the above formulas, plug D/2, d/2 in for R, r
# Eventually gives us:
# d = cuberoot(-6v / pi) + D**3

from math import pi

d, v = map(int, input().split())

while d != 0 and v != 0:
    print(((-6*v)/pi + d**3)**(1/3))

    d, v = map(int, input().split())
