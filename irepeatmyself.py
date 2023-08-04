# itertools, string processing, cycle

from itertools import cycle

n = int(input())

for i in range(n):
    line = input()

    # Try all substrings
    for j in range(1, len(line)+1):
        sub = line[:j]
        fail = False
        sub_cycle = cycle(sub)

        # Compare against cycled substring
        for k in range(len(line)):
            if line[k] != next(sub_cycle):
                fail = True
                break
        
        # Minimal subsring explains the input string
        if fail == False:
            print(len(sub))
            break

    
