n, d = map(int, input().split())

while n != 0 and d != 0:
    print(n//d, end=' ')
    print(n%d, end=' / ')
    print(d)
    
    n, d = map(int, input().split())
