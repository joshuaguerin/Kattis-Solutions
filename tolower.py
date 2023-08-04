# easy, input output, io

(p, t) = list(map(int, input().split()))

solved = p

for i in range(p):
    bad = 0
    for i in range(t):
        word = input()[1:]
        if not word.islower():
            bad = 1

    solved -= bad
        
print(solved)

                
        
