# easy, strings, comparisons

(fst, snd) = input().split()
fst = fst[::-1]
snd = snd[::-1]

if int(fst) > int(snd):
    print(fst)
else:
    print(snd)

