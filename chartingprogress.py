# strings, string processing, easy, arithmetic, 2d arrays

import sys

def process(grid):
    length = len(grid[0])-1
    offset = 0
    for l in grid:
        count = l.count('*')
        # the whole problem boils down to the following concatenation
        print('.' * (length-count-offset), "*" * count, '.' * offset, sep='')
        offset += count

        
grid = []
first = True

# required because of "read until eof"
for line in sys.stdin:
    if line != '\n':
        grid.append(line)
    else:
        if first:
            first = False
        else:
            print()
            
        process(grid)
        grid = []

# process grid at eof
if not first:
    print()
process(grid)    

