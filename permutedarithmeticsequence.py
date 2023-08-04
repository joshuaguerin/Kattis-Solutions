
def arithmetic(s):
    delta = s[1] - s[0]
    for i in range(1, len(s)-1):
        if s[i+1] - s[i] != delta:
            return False
    return True


def permuted_arithmetic(s):
    s.sort()
    delta = s[1] - s[0]
    for i in range(1, len(s)-1):
        if s[i+1] - s[i] != delta:
            return False
    return True

n = int(input())

for i in range(n):
    line = input()
    temp, *seq = line.split()
    seq = list(map(int, seq))
    
    if arithmetic(seq):
        print("arithmetic")
    elif permuted_arithmetic(seq):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")

    
    
    
