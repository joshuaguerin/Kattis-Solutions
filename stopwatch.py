# easy, simulation, array
# https://open.kattis.com/problems/stopwatch

n = int(input())
a = []
secs = 0

for i in range(n):
    a.append(int(input()))
    
if len(a)%2 == 1:
    print("still running")
    exit()

for i in range(1, len(a), 2):
    secs += a[i] - a[i-1]

print(secs)


