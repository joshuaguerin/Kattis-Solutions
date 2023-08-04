name = list(input())

i = 0

# Run through, deleting repeated characters
while i < len(name)-1:
    if name[i] == name[i+1]:
        del name[i+1]
    else:
        i += 1

# Print the result as a string
print(''.join(name))

