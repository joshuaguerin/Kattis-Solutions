# Sorted input: largest: a, b, c, d :smallest

# E.g., 1
# a=4, b=3, c=2, d=1
#     3 b
#     ___
#   _|___| 1 d
#2 c | 4 a
# order: a, d, b, c


# E.g., 2
# a=4, b=4, c=4, d=3
#     4 b
#    ____
# 4 |    | 3 d
# c |    |
#   |____|
#   | 4 a
# order: a, d, b, c

# Hypothesis: rectangle: a, d, b, c
# Size defined by b * d

values = list(map(int, input().split()))
values.sort()
print(values[0] * values[2])

