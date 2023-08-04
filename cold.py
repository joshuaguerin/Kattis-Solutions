# lambda, functional, easy

n = int(input())

print(sum(list(map(lambda temp: 1 if int(temp) < 0 else 0, input().split()))))
