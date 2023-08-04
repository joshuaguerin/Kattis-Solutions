
# Don't worry about parameters, just use globals
first = True
second = False
third = False

# 'a' switch
def call_a():
    global first, second
    temp = second
    second = first
    first = temp

# 'b' switch
def call_b():
    global second, third
    temp = second
    second = third
    third = temp

# 'c' switch
def call_c():
    global first, third
    temp = first
    first = third
    third = temp


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

