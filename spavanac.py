line = input()

(h, m) = line.split()
h = int(h)
m = int(m)

if m > 45:
    print(h, m-45)
else:
    if h == 0:
        h = 24
    print(h-1, 60-(45-m))
