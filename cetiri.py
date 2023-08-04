# easy, arithmetic sequence, brute force, conditionals

ns = list(map(int, input().split()))
ns.sort()

# next greatest number
if ns[1] - ns[0] == ns[2] - ns[1]:
    print(ns[2] + ns[2] - ns[1])
# number is between [1] and [2]
elif ns[1] - ns[0] < ns[2] - ns[1]:
    print(ns[1] + ns[1] - ns[0])
# number is between [0] and [1]
else:
    print(ns[0] + ns[2] - ns[1])

