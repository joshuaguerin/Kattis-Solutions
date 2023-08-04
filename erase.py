
def flip(sequence):
    new = []
    for c in sequence:
        new.append('0' if c == '1' else '1')
    return new

n = int(input())
fst = list(input())
snd = list(input())

if n%2 == 0 and fst == snd:
    print("Deletion succeeded")
elif n%2 == 1 and snd == flip(fst):
    print("Deletion succeeded")
else:
    print("Deletion failed")

    
