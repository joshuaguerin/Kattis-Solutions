
# 1 citation = 1 bribe
# factor = citations / articles so:
# citations = articles * factor

# however when we round up we do not need quite this many
# compute the number needed for the _previous_factor_, and add 1:

# bribes = articles*(factor-1)+1

(a, f) = list(map(int, input().split()))

print(a*(f-1)+1)

