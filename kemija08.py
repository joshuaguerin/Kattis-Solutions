


# Note: Naive string replacement will fail in test cases
#       New substrings can be created that are false positives

line = input()

vowels = ['a', 'e', 'i', 'o', 'u']

i = 0
while i < len(line):
    c = line[i]
    print(c, end='')
    i += 1
    if c in vowels:
        i += 2
print()
