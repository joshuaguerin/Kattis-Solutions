# easy, data structures, counting, input/output

n = int(input())

for i in range(n):
    _ = int(input())
    guests = list(map(int, (input().split())))

    h = {}
    
    for g in guests:
        if g not in h:
            h[g] = 1
        else:
            del(h[g])
    key = list(h.keys())[0]
    print("Case #", i+1, ": ", key, sep='')

