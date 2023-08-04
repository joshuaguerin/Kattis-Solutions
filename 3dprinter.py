from math import *

n = int(input())

# print enough printers, add a day to print
days = log(n,2) + 1

# add one more day if n is not a power of 2
if days != int(days):
    days += 1
    
print(int(days))
