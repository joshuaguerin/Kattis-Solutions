# itertools, combinations, arithmetic

from itertools import combinations_with_replacement

# Generate dictionary of possible scores
scores = {}
for i in range(1, 21):
    scores[i] = "single " + str(i)
for i in range(1, 21):
    if (2*i) not in scores:
        scores[2*i] = "double " + str(i)
    if (3*i) not in scores:
        scores[3*i] = "triple " + str(i)

n = int(input())

keys = [i for i in  list(scores.keys()) if i <= n]

# Brute force seems to be tractable (1..3 combinations w/replacement)
key_combs = list(combinations_with_replacement(keys, 1)) + list(combinations_with_replacement(keys, 2)) + list(combinations_with_replacement(keys, 3))

found = False
output = []

# Try all combinations
for comb in key_combs:
    # Combination found
    if sum(comb) == n:
        output = comb
        found = True

if found:
    for i in output:
        print(scores[i])
else:
    print("impossible")

