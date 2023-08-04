# easy, patterns, arithmetic

n = int(input())

x = 2

# pattern for the number of points on a line:
# 2, 3, 9, 17, 33 (double previous, subtract 1)

for i in range(n):
    x = 2 * x - 1

# square the result to get the grid
print(x**2)
