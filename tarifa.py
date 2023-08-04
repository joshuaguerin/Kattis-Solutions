x = int(input())
n = int(input())

megabytes = x * (n+1)
for i in range(n):
    used = int(input())
    megabytes = megabytes - used

print(megabytes)
