n = int(input())

# ordered dict would work too (possibly better)
d = {}
keys = []

# Add entries to dictionary, keylist
for i in range(n):
    (first, second) = input().split()
    try:
        first = int(first)
        first = first // 2
    except ValueError:
        first, second = second, first
        first = int(first)
    d[first] = second
    keys.append(first)

keys.sort()

# print keys in order
for k in keys:
    print(d[k])

    
