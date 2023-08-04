from sys import exit

line = input()

ops = "+-*/"

for op in ops:
    attempt = line
    attempt = attempt.replace(" ", "==", 1)
    attempt = attempt.replace(" ", op, 1)
    if eval(attempt) == True:
        print(attempt.replace("==", "=", 1))
        exit()

for op in ops:
    attempt = line
    attempt = attempt.replace(" ", op, 1)
    attempt = attempt.replace(" ", "==", 1)
    if eval(attempt) == True:
        print(attempt.replace("==", "=", 1))
        exit()




