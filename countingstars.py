# floodfill, recursion, recursion limit, 2d arrays

import sys

# 100x100 max grid, adding an extra 0 just in case
sys.setrecursionlimit(100000)

def floodfill(grid, r, c, curr, repl):
    if 0 <= r and r < len(grid):
        if 0 <= c and c < len(grid[r]):
            
            if grid[r][c] == curr:
                grid[r][c] = repl

                # floodfill n, s, w, e
                floodfill(grid, r-1, c, curr, repl)
                floodfill(grid, r+1, c, curr, repl)
                floodfill(grid, r, c-1, curr, repl)
                floodfill(grid, r, c+1, curr, repl)

case = 1
                
# required because of "read until eof"
for line in sys.stdin:
    (m, n) = list(map(int, line.split()))

    grid = []

    if m == 0:
        print("Case ", case, ": 0", sep='')
        case += 1
        continue
        
    for i in range(m):
        current = input()
        grid.append(list(current))

    if n == 0:
        print("Case ", case, ": 0", sep='')
        case += 1
        continue
    

    floods = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '-':
                floodfill(grid, i, j, '-', '#')
                floods += 1
                
    print("Case ", case, ": ", floods, sep='')

    case += 1

