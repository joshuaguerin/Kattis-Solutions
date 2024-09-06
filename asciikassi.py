# easy, ascii art, matrix

n = int(input())

horiz = '+' + '-'*n + '+'

print(horiz)
for i in range(n):
    print('|' + ' '*n + '|')
print(horiz)
