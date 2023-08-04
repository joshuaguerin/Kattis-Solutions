
n = int(input())
binary = []

while(n > 0):
    binary.append(n%2)
    n = n // 2

binary.reverse()

new = 0

for i in range(len(binary)):
    if binary[i] == 1:
        new += 2**i

print(new)


