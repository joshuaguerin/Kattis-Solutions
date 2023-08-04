n = int(input())

names = []

# Get names
for i in range(n):
    current = input()
    names.append(current)

# Sort in ascending, descending
ascending = names.copy()
ascending.sort()
descending = names.copy()
descending.sort()
descending.reverse()

# Evaluate result
if names == ascending:
    print("INCREASING")
elif names == descending:
    print("DECREASING")
else:
    print("NEITHER")

