
# All of the real work is here
def left(grid):
    new = []
    for line in grid:
        #print(line)
        # 0s aren't needed
        while 0 in line:
            line.remove(0)
        #print(line)
        i = 0
        # combine like tiles
        while i < len(line)-1:
            #print(line[i], line[i+1])
            if line[i] == line[i+1]:
                line[i] += line[i+1]
                del line[i+1]
            i += 1
        line.extend([0] * (4 - len(line)))
        new.append(line)
    return new


def right(grid):
    # reverse
    for i in range(4):
        grid[i].reverse()
    # send left
    left(grid)
    # reverse again
    for i in range(4):
        grid[i].reverse()
    return grid


def up(grid):
    # transpose, make 2d list, push left
    new = left(list(map(list, list(zip(*grid)))))
    # transpose back, make list, return
    return list(map(list, list(zip(*new))))

def down(grid):
    # transpose, make 2d list, push right
    new = right(list(map(list, list(zip(*grid)))))
    # transpose back, make list, return
    return list(map(list, list(zip(*new))))

    
grid = []

# read grid
for i in range(4):
    grid.append(list(map(int, input().split())))

move = int(input())

# apply move
if move == 0:
    new = left(grid)
elif move == 1:
    new = up(grid)
elif move == 2:
    new = right(grid)
elif move == 3:
    new = down(grid)

# print result
for line in new:
    for num in line:
        print(num, end=' ')
    print()




