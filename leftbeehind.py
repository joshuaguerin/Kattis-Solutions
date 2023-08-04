# conditionals, loops

(sweet, sour) = list(map(int, input().split()))

while sweet+sour != 0:
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet == sour:
        print("Undecided.")
    elif sweet > sour:
        print("To the convention.")
    else:
        print("Left beehind.")
        
    (sweet, sour) =list(map(int, input().split()))
