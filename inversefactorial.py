
from sys import exit
from math import log

# cache factorials smaller than 10
facts = {1:1, 2:2, 6:3, 24:4, 120:5, 720:6, 5040:7, 40320:8, 362880:9, 3628800:10}

# print if smaller than 10
f = input()
fact_len = len(f)

if fact_len <= 7:
    print(facts[int(f)])
    exit()

# if greater than 10, compute by length of factorial
i = 1
running_log = 0
while True:
    running_log += log(i, 10)
    if int(running_log)+1 == fact_len:
        print(i)
        exit()
    i += 1
