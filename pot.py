n = int(input())
output = 0

for i in range(n):
    next = input()
    pow = next[-1]
    next = next[0:len(next)-1]
    
    next = int(next)
    pow = int(pow)

    output += next**pow

print(output)
