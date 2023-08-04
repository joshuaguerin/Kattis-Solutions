# bipartite graph partitioning, 2-coloring, breadth first search, bfs

# For BFS
from queue import Queue

n = int(input())

# Names to ints and vice-versa
names = {}
names_rev = []
# Edge list int->[int]
edges = {}
vertices = set()

# Initialize forward, backward list of names
for i in range(n):
    current = input()
    names[current] = i
    names_rev.append(current)

# Initialize colors
color = [float('inf')] * len(names)
    
m = int(input())

start = ""

# Initialize adjacency list (both directions)
for i in range(m):
    (fst, snd) = input().split()
    fst = names[fst]
    snd = names[snd]
    if not fst in edges:
        edges[fst] = []
    if not snd in edges:
        edges[snd] = []
    edges[fst].append(snd)
    edges[snd].append(fst)
    vertices.add(fst)

# BFS starting with every fst in (fst, snd)
for e in edges:
    # color is assigned
    if color[e] != float('inf'):
        continue
    
    q = Queue()
    q.put(e)

    color[e] = 0

    # perform BFS
    while not q.empty():
        fst = q.get()
        for snd in edges[fst]:
            if color[snd] == float('inf'):
                color[snd] = 1 - color[fst]
                q.put(snd)
            elif color[fst] == color[snd]:
                # failure
                print("impossible")
                exit()

# Print Walter's list
for i in range(len(color)):
    if color[i] == 0:
        print(names_rev[i], end=' ')

print()

# Jesse gets everything else
for i in range(len(color)):
    if color[i] != 0:
        print(names_rev[i], end=' ')

print()
