
# Don't worry about parameters, just use globals
first = True
second = False
third = False

# 'a' switch
def call_a():
    global first, second
    first, second = second, first

# 'b' switch
def call_b():
    global second, third
    second, third = third, second

# 'c' switch
def call_c():
    global first, third
    first, third = third, first

swaps = input()

# Perform swaps
for c in swaps:
    if c == 'A':
        call_a()
    elif c == 'B':
        call_b()
    else:
        call_c()

# Print final location
if first:
    print(1)
elif second:
    print(2)
else:
    print(3)

