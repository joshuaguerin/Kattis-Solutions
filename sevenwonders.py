line = input()

T = 0
C = 0
G = 0

for c in line:
    if c == 'T':
        T += 1
    elif c == 'C':
        C += 1
    else:
        G += 1

print(T**2 + C**2 + G**2 + min(T, C, G)*7)

