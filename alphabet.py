# medium, dynamic programming, dp, lcs, longest common subsequence

# input's proximity to an "alphabet" is the length
# of the lcs with the actual alphabet
first = "abcdefghijklmnopqrstuvwxyz"

second = input()

# lcs_length, print_lcs from CLRS3e
def lcs_length(x, y):
    m = len(x)
    n = len(y)
    b = []
    c = []

    for i in range(m+1):
        b.append([0] * (n+1))
        c.append([0] * (n+1))

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i+1][j+1] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i+1][j+1] = '|'
            else:
                c[i][j] = c[i][j-1]
                b[i+1][j+1] = '-'
    return (c, b)
    
(c, b) = lcs_length(first, second)

out = []

def print_lcs(b, x, i, j):
    if i==0 or j==0:
        return
    if b[i][j] == '\\':
        print_lcs(b, x, i-1, j-1)
        out.append(x[i-1])
        #print(x[i-1])
    elif b[i][j] == '|':
        print_lcs(b, x, i-1, j)
    else:
        print_lcs(b, x, i, j-1)

print_lcs(b, first, len(first), len(second))
print(26-len(out))
