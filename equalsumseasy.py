# itertools, brute force, greedy, easy, data structures
# score: 2.49 s

from itertools import *

# the problem is marked as easy, going to try brute force
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


t = int(input())

for i in range(t):
    print("Case #", i+1, ':', sep='')
    sum_dict = {}
    
    (ignore, *line) = input().split()
    nums = set(map(int, line))

    # generate all subsets
    combos = powerset(nums)
    combos = list(combos)

    for combo in combos:
        s = sum(combo)

        # accumulate sums/subsets in a dict
        if not s in sum_dict:
            sum_dict[s] = []
            sum_dict[s].append(combo)
        else:
            sum_dict[s].append(combo)
            # get out early if a combo is found
            break

    keys = list(sum_dict.keys())
    keys.sort()

    success = False
    # if a pair of like sums is found, print it
    for k in keys:
        if len(sum_dict[k]) > 1:
            for elem in sum_dict[k][0]:
                print(elem, end=' ')
            print()
            for elem in sum_dict[k][1]:
                print(elem, end=' ')
            print()
            
            success = True
            break
    
    if not success:
        print("Impossible")


