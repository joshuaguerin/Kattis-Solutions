# Input three coordinates
c1 = input().split()
c2 = input().split()
c3 = input().split()

# Create list of x values
xs = [c1[0], c2[0], c3[0]]
# Create list of y x values
ys = [c1[1], c2[1], c3[1]]

# Duplicates are now next to each other
xs.sort()
ys.sort()

# Print x and y values that occur once
if xs[0] == xs[1]:
    print(xs[2], end=' ')
else:
    print(xs[0], end=' ')

if ys[0] == ys[1]:
    print(ys[2], end=' ')
else:
    print(ys[0], end=' ')



