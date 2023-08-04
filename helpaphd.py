n = int(input())

for i in range(n):
    problem = input()
    if problem.find('+') != -1:
        print((eval(problem)))
    else:
        print("skipped")
