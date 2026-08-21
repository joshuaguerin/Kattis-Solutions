# Easy, strings, filter, join, lambda
# https://open.kattis.com/problems/leynithjonusta
# Link included to avoid thorn in file name.

print(''.join(list(filter(lambda x: not str.isspace(x), input()))))
