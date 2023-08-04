# easy, io


# Note: The order given is no the required order of traversal.
# Start at the farthest on either side, traverse twice to get back.

t = int(input())

for i in range(t):
    n = int(input())
    dists = list(map(int, input().split()))

    high = max(dists)
    low = min(dists)

    print(2 * (high - low))


