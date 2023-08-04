from math import *

# x = v * t * cos(theta) so:
# t =     x
#     ---------
#      v * cos(theta)

g = 9.81

n = int(input())

for i in range(n):
    (v, theta, x, h1, h2) = list(map(float, input().split()))
    theta = radians(theta)
    t = x / (v * cos(theta))
    y = v * t * sin(theta) - .5 * g * t**2
    if (y-1) > h1 and (y+1) < h2:
        print("Safe")
    else:
        print("Not Safe")

