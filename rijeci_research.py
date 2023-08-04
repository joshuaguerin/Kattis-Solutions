screen = 'A'

k = int(input())

for i in range(k):
    new_screen = ""

    for c in screen:
        if c == "A":
            new_screen += "B"
        else:
            new_screen += "BA"

    screen = new_screen

print(screen.count("A"), screen.count("B"))

