from sys import exit

current = int(input())
current -= 1
questions = int(input())
elapsed = 0

for i in range(questions):
    time, outcome = input().split()
    time = int(time)

    elapsed += time
    if elapsed > 210:
        print(current+1)
        exit()
        
    if outcome == "T":
        current = (current + 1)%8


print(current + 1)

