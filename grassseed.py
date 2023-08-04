c = float(input())
l = int(input())

total = 0

for i in range(l):
    (length, width) = list(map(float, input().split()))
    total = total + (length * width)

print(total * c)

