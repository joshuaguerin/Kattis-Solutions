from math import sqrt

n = int(input())

# Given the 1 second limit I doubt rotating
# the matrix is in the cards.

for i in range(n):
    line = input()
    length = len(line)
    width = int(sqrt(length))

    for j in range(0, width):
        for k in range(width-1-j, length, width):
            print(line[k], end="")

    print()
        


