# easy, string processing

vs = "aeiouAEIOU"

total = 0

for c in input():
    if c in vs:
        total += 1

print(total)
