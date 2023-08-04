n = int(input())

for i in range(n):
    first = input()
    second = input()

    print(first, second, sep='\n')
    
    for i in range(len(first)):
        if first[i] == second[i]:
            print('.', end='')
        else:
            print('*', end='')
    print(end='\n\n')
