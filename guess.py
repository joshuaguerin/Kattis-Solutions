# easy, arithmetic, game, input output

import sys

start = 1
end = 1000
answer = "lower"

while answer != "correct":
    print((end + start)//2)
    sys.stdout.flush()
    answer = input()
    if answer == "correct":
        exit(0)
    
    if answer == "lower":
        end = (end + start)//2-1
    elif answer == "higher":
        start = (end + start)//2+1


