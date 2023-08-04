# discrete, primes, math

def sieve(max):
    isPrime = list(range(max))
    #p: 2,3,4,...,sqrt(N)
    for p in range(2,int(max**0.5)+1): 
        if isPrime[p]:
            #p^2, p^2+p, p^2+2p, ..., N
            for multiple in range(p**2,max,p):
                isPrime[multiple] = False
    return [x for x in isPrime[2:] if x]

def happy(p):
    # for cycle detection in happy search
    values = set()
    
    current = p
    # Search for happiness
    while current != 1 and current not in values:
        values.add(current)
        current = list(str(current))
        current = list(map(int, current))
        current = list(map(lambda x: x**2, current))
        current = sum(current)

    if current in values:
        return False
    else:
        return True

primes = set(sieve(10000))

n = int(input())
for i in range(1, n+1):
    (_, p) = input().split()
    p = int(p)

    if p in primes and happy(p):
        print(i, p, "YES")
    else:
        print(i, p, "NO")
    

