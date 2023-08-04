# simple, strings, 2d arrays

def validate(grid, i, j):
    moves = 0
    if 1 < i and grid[i-2][j] == '.' and grid[i-1][j] == 'o':
        moves += 1
    if 1 < j and grid[i][j-2] == '.' and grid[i][j-1] == 'o':
        moves += 1
    if i < 5 and grid[i+2][j] == '.' and grid[i+1][j] == 'o':
        moves += 1
    if j < 5 and grid[i][j+2] == '.' and grid[i][j+1] == 'o':
        moves += 1
    return moves
        
grid = []

for i in range(7):
    grid.append(input())

total = 0
for i in range(7):
    for j in range(7):
        
        if grid[i][j] == 'o':
            total += validate(grid, i, j)
print(total)
