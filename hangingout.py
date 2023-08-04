(L, x) = list(map(int, input().split()))

current = 0
denied = 0

for i in range(x):
    (action, num) = input().split()
    num = int(num)
    if action == "enter" and num+current <= L:
        current += num
    elif action == "leave":
        current -= num
    else:
        denied += 1
    
print(denied)
