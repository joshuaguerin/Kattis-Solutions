
def sieve(max):
    isPrime = list(range(max))
    #p: 2,3,4,...,sqrt(N)
    for p in range(2,int(max**0.5)+1): 
        if isPrime[p]:
            #p^2, p^2+p, p^2+2p, ..., N
            for multiple in range(p**2,max,p):
                isPrime[multiple] = False
    return [x for x in isPrime[2:] if x]


primes = sieve(32000)

n = int(input())
primes_s = set(primes)

for i in range(n):
    x = int(input())
    
    sums = []

    # note: naive double-for solution (quadratic) will not work
    for p in primes:
        candidate = x - p
        if candidate < p:
            break

        # note: set inclusion is O(1) average, O(n) worst case
        if candidate in primes_s:
            sums.append(str(p) + "+" + str(candidate))
    
    print(x, "has", len(sums), "representation(s)")
    for s in sums:
        print(s)

