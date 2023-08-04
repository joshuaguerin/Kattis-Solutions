# easy, string processing, length

import sys

text = []

# required because of "read until eof"
for line in sys.stdin:
    text.append(line[:-1])

n = max(map(len, text))

score = 0

for i in range(len(text)-1):
    score += (n - len(text[i]))**2
print(score)



