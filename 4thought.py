# itertools, combinations, permutations, replacement, eval, strings, data structures

from itertools import combinations_with_replacement as combs_r
from itertools import permutations as perms

op_map = {}
tabu = set()

# generate all possible mappings (turns out not many)
for (fst, snd, thd) in combs_r(['+', '-', '//', '*'], 3):
    for (f, s, t) in perms([fst, snd, thd], 3):
        e = eval('4' + f + '4' + s + '4' + t + '4')

        # new entry
        if e not in op_map:
            if f == '//':
                f = '/'
            if s == '//':
                s = '/'
            if t == '//':
                t = '/'

            # store
            op_map[e] = '4 ' + f + ' 4 ' + s + ' 4 ' + t + ' 4'
            
n = int(input())

for i in range(n):
    val = int(input())
    if val in op_map:
        print(op_map[val], '=', val)
    else:
        print("no solution")

