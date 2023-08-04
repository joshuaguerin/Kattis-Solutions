n = int(input())

for i in range(n):
    line = input()
    k = int(len(line)**.5 + .5)
    k_square = k**2
    
    line += '*' * (k_square - len(line))
    
    matrix = []

    index = 0

    # build matrix
    for i in range(k):
        row = []
        for j in range(k):
            row.append(line[index])
            index += 1
        matrix.append(row)

    # print matrix
    for i in range(0, k):
        for j in range(k-1, -1, -1):
            if matrix[j][i] != '*':
                print(matrix[j][i], end='')
    print()

