# string processing, string searching, numerical bases, hex, discreteA

import sys

# required because of "read until eof"
for line in sys.stdin:
        candidates = []
        
        # Process 0x 0X as separate cases
        index = line.find('0x')
        while index != -1:
                end = index+2
                while line[end] in "0123456789abcdefABCDEF":
                        end += 1
                candidates.append((index, line[index:end]))

                index = line.find('0x', end)

        # Copy-paste magic for 0X
        index = line.find('0X')
        while index != -1:
                end = index+2
                while line[end] in "0123456789abcdefABCDEF":
                        end += 1
                candidates.append((index, line[index:end]))

                index = line.find('0X', end)
        
        # Sort according to their indices
        candidates.sort()
        
        # Output Results
        for c in candidates:
                print(c[1], int(c[1], 16))



