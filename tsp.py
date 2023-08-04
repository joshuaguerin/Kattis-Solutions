# greedy, easy
# score: (3.006318)

from math import sqrt

def distance(x, y):
    return sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2)

n = int(input())

cities = []


for i in range(n):
    line = input()
    (x, y) = line.split()
    x = float(x)
    y = float(y)

    cities.append((x, y))


tour = []
tour.append(0)

candidates = list(range(1, n))

while(len(candidates) > 0):
    best = candidates[0]
    best_dist = distance(cities[tour[-1]], cities[best])
    
    for i in range(1, len(candidates)):
        if distance(cities[tour[-1]], cities[candidates[i]]) < best_dist:
            best = candidates[i]
            best_dist = distance(cities[tour[-1]], cities[candidates[i]])
    
    tour.append(best)
    candidates.remove(best)

for c in tour:
    print(c)
