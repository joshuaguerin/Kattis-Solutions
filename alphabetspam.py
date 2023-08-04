line = input()

white = 0
lower = 0
upper = 0
special = 0

for c in line:
    if c == '_':
        white += 1
    elif 'a' <= c and c <= 'z':
        lower += 1
    elif 'A' <= c and c <= 'Z':
        upper += 1
    else:
        special += 1


length = len(line)
print(white/length, lower/length, upper/length, special/length, sep='\n')

