d = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6', 'h':'[-]', 'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]', 'n':'[]\[]', 'o':'0', 'p':'|D', 'q':'(,)', 'r':'|Z', 's':'$', 't':"']['", 'u':'|_|', 'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/', 'z':'2'}

line = input()
line = line.lower()

letters = "abcdefghijklmnopqrstuvwxyz"

for c in line:
    if c in letters:
        print(d[c], end='')
    else:
        print(c, end='')

print()

