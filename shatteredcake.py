# easy, geometry, rectangles
# https://open.kattis.com/problems/shatteredcake

w = int(input())
n = int(input())

area = 0


# Get the combined area
for i in range(n):
    a, b = map(int, input().split())

    area += a*b

# Reverse the other dimension
print(int(area/w))
