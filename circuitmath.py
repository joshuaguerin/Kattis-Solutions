# easy-medium, math, logic, stack, data structures

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
truths = input().split()
equation = input().split()

truths = list(map(lambda x: True if x=="T" else False, truths))
truth_map = {}
for i in range(len(truths)):
    truth_map[alpha[i]] = truths[i]

for i in range(len(equation)):
    if equation[i] in alpha:
        equation[i] = truth_map[equation[i]]

i = 0

while i < len(equation):
    if not (equation[i] in [True, False]):
        if equation[i] == '*':
            equation[i-2] = equation[i-1] and equation[i-2]
            del equation[i-1:i+1]
            i -= 1
        elif equation[i] == '+':
            equation[i-2] = equation[i-1] or equation[i-2]
            del equation[i-1:i+1]
            i -= 1
        elif equation[i] == '-':
            equation[i-1] = not equation[i-1]
            del equation[i]
    else:
        i += 1
    #print(i, equation)
    #input()

if equation[0]:
    print("T")
else:
    print("F")

