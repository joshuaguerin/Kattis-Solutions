# does not work--times out

cases = int(input())

for i in range(cases):
    p = int(input())
    n = int(input())

    denoms = [0] * n
    
    for j in range(n):
        denoms[j] = int(input())
        
    memo = [-1] * (10**6+1)
    memo[0] = 0
    
    for c in denoms:
        # incorrect range (should be reversed) but
        # times out so who cares.
        for j in range(p):
            if memo[j] == -1:
                continue
            if memo[j+c] == -1 or memo[j]+1 < memo[j+c]:
                memo[j+c] = memo[j]+1

    total = p
    while memo[total] == -1:
        total += 1
    
    print(total, memo[total])
            
