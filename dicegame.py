# dice, discrete, math, io

gunnar = sum(list(map(int, input().split())))
emma = sum(list(map(int, input().split())))

if gunnar == emma:
    print("Tie")
elif gunnar > emma:
    print("Gunnar")
else:
    print("Emma")

