n = int(input())

# There is no optimal play, just divisibility
# Hint: Each takes _exactly_ two stones
if n%2 == 0:
    print("Bob")
else:
    print("Alice")
