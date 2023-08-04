n = int(input())

while n != -1:
    total = 0
    old_t = 0
    
    for i in range(n):
        line = input()
        (s, t) = line.split()
        s = int(s)
        t = int(t)
        total += s * (t-old_t)
        old_t = t

    print(total, "miles")
        
    n = int(input())
