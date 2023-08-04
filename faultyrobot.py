# graph algorithms, reachability analysis, medium.


# Problem parameters.
(n, m) = list(map(int, input().split()))

# Configure sets/lists used.
edges = [[] for i in range(n+1)]
forced_edges = [[] for i in range(n+1)]
forced_enter = set()
forced_leave = set()

# Read graph as adjacency lists.
for i in range(m):
    (fst, snd) = list(map(int, input().split()))
    if fst > 0:
        edges[fst].append(snd)
    else:
        forced_edges[abs(fst)].append(snd)
        forced_enter.add(snd)
        forced_leave.add(abs(fst))


# Propagate all forced edges to stabilization.
visited = set()
vis_new = [1]

while len(vis_new) > 0:
    current = vis_new.pop()
    visited.add(current)

    for w in forced_edges[current]:
        if not w in visited:
            vis_new.append(w)


# Propagate _one_ accidental/faulty move beyond.
vis_new = set()

for i in range(1, n+1):
    if i in visited:
        vis_new = vis_new | set(edges[i])

visited = visited | vis_new


# Propagate all forced edges to stabilization.
# (Same as first step, but only for newly visited edges.)
vis_new = list(vis_new)

while len(vis_new) > 0:
    current = vis_new.pop()
    visited.add(current)
    
    for w in forced_edges[current]:
        if not w in visited:
            vis_new.append(w)

visited = visited | set(vis_new)

# Result: Any vertex visited that we aren't forced to leave.
resting = len(visited - forced_leave)
print(resting)


