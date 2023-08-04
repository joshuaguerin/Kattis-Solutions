n = int(input())

for i in range(n):
    line = input()
    if line[0:10] == "Simon says":
        print(line[10:])
