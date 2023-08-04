# Note: This works, but is broken due to time.
# Python3 may just not work for this sort of dp.

def greedy(n, cs):
    total = 0
    
    for i in range(len(cs)-1, -1, -1):
        div = n//cs[i]
        total += div
        n -= div*cs[i]
    return total

n = int(input())
cs = list(map(int, input().split()))

memo = [0] * (cs[-1]+cs[-2])
for c in cs:
    memo[c] = 1

for i in range(len(memo)):
    if memo[i] != 0:
        if memo[i] < greedy(i, cs):
            print('non-canonical')
            exit()
        
        for c in cs:
            if i+c < len(memo) and (memo[i+c] == 0 or memo[i]+1 < memo[i+c]):
                    memo[i+c] = memo[i]+1
print('canonical')
