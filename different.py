# On Unix:
# cat input2.txt | python3 read.py
import sys

# not sure why this proves so challenging on kattis
# perhaps an overflow of int?
for line in sys.stdin:
    x, y = list(map(int, line.split()))
    print(abs(x - y))
    
