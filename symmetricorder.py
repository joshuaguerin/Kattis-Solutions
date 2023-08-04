n = int(input())
set_num = 1

while n != 0:
    l = []
    # Read list of strings
    for i in range(n):
        current = input()
        l.append(current)

    first = []
    second = []

    # Put every other string in either first or second
    for i in range(len(l)):
        if i%2 == 0:
            first.append(l[i])
        else:
            second.append(l[i])

    # Reverse second (strings now in descending order of length)
    second.reverse()

    # Print set
    print("SET", set_num)
    for s in first:
        print(s)
    for s in second:
        print(s)


    # Get next n
    n = int(input())
    set_num += 1

