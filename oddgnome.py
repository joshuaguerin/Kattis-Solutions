n = int(input())

for i in range(n):
    (g, *gs) = list(map(int, input().split()))

    for i in range(1, g-1):
        if gs[i-1]+1 != gs[i]:
            print(i+1)
            break
