
line = input()

i=0
card = ""
cards = []
# Create a list of cards
for c in line:
    if i%3 == 0 and card != "":
        cards.append(card)
        card = ""
    
    card += c
    i += 1

# Add last card
if card != "":
    cards.append(card)
    
if len(cards) != len(set(cards)):
    print("GRESKA")
else:
    for suite in "PKHT":
        count = 13
        for c in cards:
            if c[0] == suite:
                count -= 1
        print(count, end=" ")
    print()
