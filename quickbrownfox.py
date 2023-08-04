n = int(input())

for i in range(n):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    line = input().lower()

    for c in line:
        if c in alphabet:
            alphabet.remove(c)

    letters = ''.join(alphabet)
    
    if letters == '':
        print('pangram')
    else:
        print('missing', letters)
