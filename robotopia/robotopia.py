# linear equations, brute force, algebra, math

# Explanation in the 2016 ICPC Qualifier Judge's Explanations

n = int(input())

for i in range(n):
    (l1, a1, l2, a2, lt, at) = list(map(int, input().split()))

    matched = False
    vals = '?'
    
    x = 1
    while l1 * x < lt:
        y1 = (lt - l1*x) / l2
        y2 = (at - a1*x) / a2

        #print(x, y1, y2)
        
        if y1 == y2 and y1 == int(y1) and y2 == int(y2):
            #print('matched', y1, y2)
            
            if matched == False:
                matched = True
                vals = (x, y1)
            elif matched == True:
                vals = '?'
                break

        x += 1

    if len(vals) == 2:
        print(*map(int, vals))
    else:
        print(vals)
