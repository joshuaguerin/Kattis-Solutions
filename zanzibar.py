t = int(input())

# Process each line
for i in range(t):
    # Grab line, split, int()
    turtles = input().split()
    imported = 0
    
    turtles = list(map(int, turtles))
    del turtles[-1] # 0 isn't necessary

    # Starting point
    current = turtles[0]
    del turtles[0]

    # Compute minimum imports
    for t in turtles:
        if t > 2*current:
            imported += t - (2*current)
        current = t
    
    print(imported)

