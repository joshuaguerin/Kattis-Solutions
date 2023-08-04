# easy, arithmetic, ord, chr, patterns

t = int(input())

for i in range(t):
    n = list(input())

    # search for a digit that can be decremented
    for j in range(len(n)-1, -1, -1):
        if n[j] != '0':
            n[j] = chr(ord(n[j])-1)
            break

    print(int(''.join(n)))

    
