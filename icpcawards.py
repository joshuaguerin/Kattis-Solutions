# easy, set, io, strings

n = int(input())

seen = set()
printed = 0

for i in range(n):
    line = input()
    vals = line.split()
    if vals[0] not in seen and printed<12:
        printed += 1
        seen.add(vals[0])
        print(line)
