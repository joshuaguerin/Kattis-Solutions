def fib(n):
    a, b = 0, 1
    for i in range(0, n-1):
        a, b = b, a + b
    return a

k = int(input())

print(fib(k), fib(k+1))


