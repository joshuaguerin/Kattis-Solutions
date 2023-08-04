d = {' ':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
d_rev = {x: k for k, x in d.items()}

def enc(v):
    u = [v[0]]                 # starting value
    s = [d_rev[v[0]]]          # starting character
    for i in range(1, len(v)): # encrypt/decrypt
        u.append(u[-1] + v[i])
        u[i] = u[i] % 27
        s.append(d_rev[u[i]])
    return ''.join(s)

def dec(v):
    s = [d_rev[v[0]]]

    # restore the %27
    for i in range(1, len(v)):
        while v[i] < v[i-1]:
            v[i] += 27

    u = [d_rev[v[0]]]
            
    # remove previous values
    for i in range(1, len(v)):
        u.append(v[i] - v[i-1])
        # restore character
        u[i] = d_rev[u[i]]
    
    return ''.join(u)

n = int(input())

for i in range(n):
    text = input()
    
    c = text[0]
    s = text[2:]
    v = []
    for i in range(len(s)):
        #print(s[i])
        v.append(d[s[i]])

    if c == 'e':
        u = enc(v)
    elif c == 'd':
        u = dec(v)
    
    print(u)
    
