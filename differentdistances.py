from math import *

def p_norm(x1, y1, x2, y2, p):
    return (abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p)

line = input()

while line != "0":
    x1, y1, x2, y2, p = list( map(float, line.split()) )

    print(p_norm(x1, y1, x2, y2, p))
    
    line = input()
