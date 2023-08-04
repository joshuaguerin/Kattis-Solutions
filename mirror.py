t = int(input())


for i in range(t):
    (rows, cols) = list(map(int, input().split()))
    image = []
    
    for j in range(rows):
        row = input()[::-1]
        image.append(row)

    print("Test", i+1)
    while len(image) != 0:
        print(image[-1])
        image.pop()


