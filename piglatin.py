# string processing

import sys

# required because of "read until eof"
for line in sys.stdin:
    words = line.split()
    for word in words:
        if word[0] in "aeiouy":
            print(word, "yay", sep='', end=' ')
        else:
            index = len(word)+1
            for c in "aeiouy":
                current = word.find(c)
                if current != -1 and current < index:
                    index = current
            print(word[index:], word[:index], "ay", sep='', end=' ')
    print()

