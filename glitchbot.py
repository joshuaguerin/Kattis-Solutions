(x, y) = list(map(int, input().split()))

def do(loc, curr_dir, action):
    if action == 'Forward':
        if curr_dir == 'north':
            loc[1] += 1
        elif curr_dir == 'south':
            loc[1] -= 1
        elif curr_dir == 'east':
            loc[0] += 1
        elif curr_dir == 'west':
            loc[0] -= 1
    elif action == 'Right':
        if curr_dir == 'north':
            curr_dir = 'east'
        elif curr_dir == 'east':
            curr_dir = 'south'
        elif curr_dir == 'south':
            curr_dir = 'west'
        elif curr_dir == 'west':
            curr_dir = 'north'
    elif action == 'Left':
        if curr_dir == 'east':
            curr_dir = 'north'
        elif curr_dir == 'south':
            curr_dir = 'east'
        elif curr_dir == 'west':
            curr_dir = 'south'
        elif curr_dir == 'north':
            curr_dir = 'west'
    return (loc, curr_dir)

    
n = int(input())

dirs_orig = []
for i in range(n):
    dirs_orig.append(input())


#simulate
# location_orig = [0, 0]
# curr_dir_orig = 'north'

pos = 0
    

for pos in range(n):
    dirs = dirs_orig.copy()

    # reset to start
    location = [0, 0]
    curr_dir = 'north'
    
    choices = set(['Right', 'Left', 'Forward']) - set([dirs[pos]])
    choices = list(choices)
    
    dirs[pos] = choices[0]
    
    for i in range(n):
        (location, curr_dir) = do(location, curr_dir, dirs[i])

    if x == location[0] and y == location[1]:
        print(pos+1, choices[0])
        exit()

    # reset to start
    location = [0, 0]
    curr_dir = 'north'
    
    dirs[pos] = choices[1]
    
    for i in range(n):
        (location, curr_dir) = do(location, curr_dir, dirs[i])
    
    if x == location[0] and y == location[1]:
        print(pos+1, choices[1])
        exit()
    
