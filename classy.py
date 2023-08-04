# sorting, medium, wording

from math import *

t = int(input())

for i in range(t):
    vals = []
    n = int(input())

    # Process each entry
    for j in range(n):
        (name, desig, c) = input().split()
        name = name[0:len(name)-1]
        desig = desig.split('-')

        # To maintain correct ordering (trailing is first)
        desig.reverse()

        value = []

        # Change to something quicker to compare
        for title in desig:
            if title == "upper":
                value.append(1)
            elif title == "middle":
                value.append(3)
            else:
                value.append(5)
        
        
        vals.append([value, name])

    # Pad each title up to the max
    for i in range(n):
        (val, name) = vals[i]
        while len(val) < 10:
            val.append(3)
        vals[i] = [val, name]
        
    vals.sort()
    
    for i in range(n):
        (val, name) = vals[i]
        print(name)
    print("==============================")
    
    
