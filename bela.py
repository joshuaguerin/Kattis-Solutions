# Quicker to specify as dict()s than functions
dom = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
other = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}

(n, s) = input().split()
n = int(n)

total = 0

for i in range(n):
    for i in range(4):
        card = input()
        # Add each card's value
        if card[1] == s:
            total += dom[card[0]]
        else:
            total += other[card[0]]

print(total)

