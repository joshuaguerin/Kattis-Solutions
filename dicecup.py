import itertools
from collections import *

(d1, d2) = list(map(int, input().split()))

d1 = d1 + 1
d2 = d2 + 1

# Cartesian product
combs = list(itertools.product(list(range(1, d1)), list(range(1, d2))))
sums = list(map(sum, combs))

# Create histogram ordered by counts
freqs = Counter(sums).most_common(len(sums))
freq = freqs[0][1]

# Print most common, then stop
for i in range(len(freqs)):
    if freqs[i][1] == freq:
        print(freqs[i][0])
    else:
        break;

