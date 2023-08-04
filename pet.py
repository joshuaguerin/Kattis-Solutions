
totals = []

for i in range(5):
    line = input()
    nums = line.split()
    total = 0
    for val in nums:
        total += int(val)
    totals.append(total)

print(totals.index(max(totals))+1, end=" ")
print(max(totals))



