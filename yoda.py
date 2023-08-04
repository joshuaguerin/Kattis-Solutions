fst = list(map(int, list(input())))
snd = list(map(int, list(input())))

fst.reverse()
snd.reverse()

while len(fst) < len(snd):
    fst.append(-1)
while len(snd) < len(fst):
    snd.append(-1)

new_fst = []
new_snd = []

for i in range(len(fst)):
    if fst[i] == snd[i]:
        new_fst.append(fst[i])
        new_snd.append(snd[i])
    elif fst[i] > snd[i]:
        new_fst.append(fst[i])
    else:
        new_snd.append(snd[i])

new_fst.reverse()
new_snd.reverse()

        
if new_fst == []:
    print("YODA")
else:
    print(int(''.join(list(map(str, new_fst)))))

if new_snd == []:
    print("YODA")
else:
    print(int(''.join(list(map(str, new_snd)))))
