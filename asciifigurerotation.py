# whitespace, matrix, rotations, ascii, text processing

# Note: The problem itself is relatively easy.
# Make sure that _all_excess_ whitespace is removed or
# your solution will be rejected.

def printM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='')
        print()
    print()    

n = int(input())

first = True

while n != 0:
    # avoid final \n when finished
    if not first:
        print()
    
    # read matrix
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    
    # make the matrix non-jagged
    row_width = max(list(map(len, matrix)))
    for i in range(len(matrix)):
        while(len(matrix[i]) < row_width):
            matrix[i].append(' ')
    
    # rotate matrix
    matrix = list(zip(*matrix[::-1]))
    
    # change tuples to lists
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i])
    
    # swap - and |
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '-':
                matrix[i][j] = '|'
            elif matrix[i][j] == '|':
                matrix[i][j] = '-'

    # turn rows back to strings
    for i in range(len(matrix)):
        matrix[i] = ''.join(matrix[i])
    
    # strip trailing whitespace (as per the problem)
    for i in range(len(matrix)):
        # only print lines that have nonspace characters
        if not matrix[i].isspace():
            print(matrix[i].rstrip())
            
    n = int(input())
    first = False
