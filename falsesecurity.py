# input, output, io, strings, data structures, text

morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '_':'..--', ',':'.-.-', '.':'---.', '?':'----'}

rev_morse = {v: k for k, v in morse.items()}

keys = list(morse.keys())
keys.sort()

for k in keys:
    morse[k] = list(morse[k])

import sys

# required because of "read until eof"
for line in sys.stdin:
    
    message = []
    lengths = []

    # generate Morse lists, lengths
    for c in line:
        if c != '\n':
            message.extend(morse[c])
            lengths.append(len(morse[c]))

    lengths.reverse()

    # generate new string
    i = 0
    for length in lengths:
        print(rev_morse[''.join(message[i:i+length])], end='')
        i += length
    print()

