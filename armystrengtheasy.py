t = int(input())

for i in range(t):
    # consume blank, numbers
    input()
    input()
    Ag = list(map(int, input().split()))
    Am = list(map(int, input().split()))
    Ag.sort()
    Ag.reverse()
    Am.sort()
    Am.reverse()

    # Simulate battle
    while Ag != [] and Am != []:
        if Ag[-1] == Am[-1]:
            Am.pop()
        elif Ag.count(Ag[-1]) > 1:
            Ag.pop()
        elif Am.count(Am[-1]) > 1:
            Am.pop()
        elif Ag[-1] < Am[-1]:
            Ag.pop()
        elif Am[-1] < Ag[-1]:
            Am.pop()
        else:
            break

    if Ag == Am == []:
        print("uncertain")
    if Ag == []:
        print("MechaGodzilla")
    elif Am == []:
        print("Godzilla")
    else:
        print("uncertain")
