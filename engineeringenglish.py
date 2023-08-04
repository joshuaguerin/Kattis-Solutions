
import sys

# taboo list
words = set()

# required because of "read until eof"
for line in sys.stdin:
    line = line.split()
    
    # process each word
    for word in line:
        # print only if not in taboo list
        if not word.lower() in words:
            print(word, end=' ')
            words.add(word.lower())
        else:
            print('.', end=' ')
    print()
