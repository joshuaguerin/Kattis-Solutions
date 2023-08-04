keys = input()

while keys != "0":
    line = input()
    keys = keys.split()
    k, *keys = keys
    k = int(k)
    keys = list(map(int, keys))

    # pad string
    if len(line)%k != 0:
        line += ' ' * (k - len(line)%k)

    # process string
    start = 0
    print("'", end="")
    while start < len(line):
        # process each substring
        word = line[start:start+k]

        # print characters in key order
        for i in keys:
            print(word[i-1], end="")

        # move on to next substring
        start += k
    # done
    print("'")
        
    # get next key
    keys = input()

