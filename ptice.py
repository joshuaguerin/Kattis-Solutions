
from itertools import cycle

adrian = cycle('ABC')
bruno = cycle('BABC')
goran = cycle('CCAABB')

adrian_correct = 0
bruno_correct = 0
goran_correct = 0

n = input()
exam = input()

for c in exam:
    if c == next(adrian):
        adrian_correct += 1
    if c == next(bruno):
        bruno_correct += 1
    if c == next(goran):
        goran_correct += 1

correct = max(adrian_correct, bruno_correct, goran_correct)

print(correct)
if correct == adrian_correct:
    print("Adrian")
if correct == bruno_correct:
    print("Bruno")
if correct == goran_correct:
    print("Goran")
