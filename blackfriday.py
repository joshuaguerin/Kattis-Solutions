# simple, data structures

n = int(input())
rolls = list(map(int, input().split()))
unique = set(rolls)

# keep removing the biggest until finished
while len(unique) != 0 and rolls.count(max(unique)) > 1:
    unique.remove(max(unique))

if len(unique) == 0:
    print("none")
else:
    print(rolls.index(max(unique))+1)

