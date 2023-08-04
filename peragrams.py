line = input()

letters = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for c in line:
    if not (c in letters):
        letters[c] = 1
    else:
        letters[c] += 1

remove = 0
odd_found = False

for c in alphabet:
    if c in letters and letters[c]%2 == 1:
        if not odd_found:
            odd_found = True
        else:
            remove += 1

print(remove)
