# easy, data structures, sets
# https://open.kattis.com/problems/knotknowledge

input()

# Quick set difference
all = set(input().split())
learned = set(input().split())

# Grab the one element
print(list(all - learned)[0])
