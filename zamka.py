# Add up digits (div// and mod%)
def sum_digits(i):
    sum = 0
    
    while(i > 0):
        # get least digit
        sum = sum + (i%10)
        # shift digits left
        i = i // 10
    return sum



l = int(input())
d = int(input())
x = int(input())

largest = l
smallest = d

# brute-force once going up
for i in range(l, d+1):
    sum = sum_digits(i)
    if sum == x:
        largest = i

# and again, going back
for i in range(d, l-1, -1):
    sum = sum_digits(i)
    if sum == x:
        smallest = i

print(smallest)
print(largest)
