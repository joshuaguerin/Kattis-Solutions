# easy, brute force

x = input()
digits = list(x)
digits.sort()
x = int(x)

current = x+1

# check each number greater than x
for i in range(1000000):
    current_digits = list(str(current))
    current_digits.sort()

    # finish if the digits are the same
    if current_digits == digits:
        print(current)
        exit()
    # finish if there are too many digits
    if len(current_digits) > len(digits):
        print(0)
        exit()
    
    current += 1

print(0)
