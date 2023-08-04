# arithmetic, math

# Generate conversions with Python3 shell
to_thou = {"inch":1000, "foot":12000, "yard":36000, "chain":792000, "furlong":7920000, "mile":63360000, "league":190080000, "in":1000, "ft":12000, "yd":36000, "ch":792000, "fur":7920000, "mi":63360000, "lea":190080000, "thou":1, "th":1}

(dist, start, nil, end) = input().split()
dist = int(dist)

# Convert anything to thou, then back.
print((dist * to_thou[start]) / to_thou[end])


