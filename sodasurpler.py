(e, f, cost) = list(map(int, input().split()))


bottles = e + f
total = 0

while bottles >= cost:
    bottles -= cost
    bottles += 1
    total += 1

print(total)
    
