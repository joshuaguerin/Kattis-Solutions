# python, number theory, base, bases, easy

n = int(input())

for i in range(1, n+1):
    (temp, num) = input().split()

    # watch out, may be a valid number with leading zeros
    num_i = int(num)
    try:
        print(i, int(num, 8), num_i, int(num, 16))
    except:
        print(i, 0, num_i, int(num, 16))

