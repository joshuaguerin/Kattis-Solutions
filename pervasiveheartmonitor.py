# easy, sum, casting, exceptions

import sys

# required because of "read until eof"
for line in sys.stdin:
        sum_points = 0
        count = 0
        name = []
        
        data = line.split()
        for d in data:
                # the only real work: float vs. string
                try:
                        x = float(d)
                        sum_points += x
                        count += 1
                except:
                        name.append(d)
        print(sum_points/count, end='')
        for n in name:
                print(' ', n, end='', sep='')
        print()

