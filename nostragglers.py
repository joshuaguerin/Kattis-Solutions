# easy, simulation, counting, io
# https://open.kattis.com/problems/nostragglers

n = int(input())

current = 0

for i in range(n):
    category, io, num = input().split()
    num = int(num)

    if io == "IN":
        current += num
    else:
        current -= num

if current == 0:
    print("NO STRAGGLERS")
else:
    print(current)

