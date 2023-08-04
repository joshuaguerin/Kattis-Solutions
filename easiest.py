# Add up digits (div// and mod%)
def sum_digits(i):
    sum = 0
    
    while(i > 0):
        # get least digit
        sum = sum + (i%10)
        # shift digits left
        i = i // 10
    return sum

n = int(input())

while n != 0:
    # p>10
    p = 11

    # We should be able to brute-force
    while sum_digits(n) != sum_digits(n*p):
        p+= 1

    # Broke out of the loop--found p
    print(p)

    n = int(input())
