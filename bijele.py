

line = input()
chess = line.split()

# Compute each directy, print
# Put each on the same line
print(1 - int(chess[0]),end=" ")
print(1 - int(chess[1]),end=" ")
print(2 - int(chess[2]),end=" ")
print(2 - int(chess[3]),end=" ")
print(2 - int(chess[4]),end=" ")
print(8 - int(chess[5]))

