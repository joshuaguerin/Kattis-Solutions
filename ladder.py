
# given:
#               /|
#              / |
#             /  |
# hypotenuse /   |
#      ?    /    |
#          /     | h (opposite)
#         /      |
#        /       |
# theta /v_______|
#   Compute: the hypotenuse
#    sin(theta) = opposite / hypotenuse
# so hypotenuse = opposite / sin(theta)

from math import radians, sin, ceil


line = input()
(opposite, theta) = line.split()
opposite = int(opposite)
theta = int(theta)

# Note: docs show that sin takes input in radians
hypotenuse = ceil(opposite / sin(radians(theta)))

print(hypotenuse)

