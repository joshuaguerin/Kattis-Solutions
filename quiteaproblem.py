# string processing

import sys

# required because of "read until eof"
for line in sys.stdin:
    line = line.lower()
    if "problem" in line:
        print("yes")
    else:
        print("no")

