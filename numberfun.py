n = int(input())

for i in range(n):
    ns = list(map(int, input().split()))
    
    if ns[0] + ns[1] == ns[2] or ns[0] - ns[1] == ns[2] or ns[0] * ns[1] == ns[2] or ns[0] / ns[1] == ns[2] or ns[1] - ns[0] == ns[2] or ns[1] / ns[0] == ns[2]:
        print("Possible")
    else:
        print("Impossible")
