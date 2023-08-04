# math, trick, easy

from math import sqrt

(n, w, h) = list(map(int, input().split()))

# (simple) trick question
# hypotenuse is the largest dimension that can fit
dim = sqrt(w**2 + h**2)

for i in range(n):
    l = int(input())
    
    if l <= dim:
        print("DA")
    else:
        print("NE")

