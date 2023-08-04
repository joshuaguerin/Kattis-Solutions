(R, C, Zr, Zc) = input().split()

R = int(R)
Zr = int(Zr)
Zc = int(Zc)

matrix = []

for i in range(R):
    l = input()
    matrix.append(l)

# Turn the list of strings into a list of lists of chars
chars = list(map(list, matrix))
# Flatten into a list of chars
# Turn to a set to a list to get distinct chars
chars = list(set([c for elem in chars for c in elem]))

# Add columns
for i in range(len(matrix)):
    for c in chars:
        matrix[i] = matrix[i].replace(c, c*Zc)

# Print rows
for line in matrix:
    for i in range(Zr):
        print(line)

