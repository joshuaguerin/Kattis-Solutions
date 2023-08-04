# combinatorics, itertools

from itertools import combinations

n = int(input())

while n != -1:
    weak = []
    graph = []
    
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # search each vertex for a triad in the graph
    for i in range(n):
        # get indices of all connected edges
        connected = [i for i,x in enumerate(graph[i]) if x==1]

        # trivially weak (insufficient edges)
        if len(connected) < 2:
            weak.append(i)
            continue

        # enumerate all candidates for triadic closure
        combs = combinations(connected, 2)

        triad = 0
        # search candidates for a triad
        for (fst, snd) in combs:
            if graph[fst][snd] == 1:
                triad = 1
                break
        if triad == 0:
            weak.append(i)

    for i in weak:
        print(i, end=' ')
    print()
        
    n = int(input())
    
