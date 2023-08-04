# Python3 may not be the right choice due to efficiency

class union_find:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*(n)
    def _find(self, i):
        while self.p[i] != i:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
        return i
    def find(self, i, j):
        return self._find(i) == self._find(j)
    def union(self, i, j):
        ii = self._find(i)
        jj = self._find(j)
        if ii == jj:
            return
        if self.rank[ii] > self.rank[jj]:
            self.p[jj] = ii
        else:
            self.p[ii] = jj
            if self.rank[ii] == self.rank[jj]:
                self.rank[jj]+=1
    
(n, q) = list(map(int, input().split()))

uf = union_find(n)
for i in range(q):
    (op, a, b) = input().split()
    a = int(a)
    b = int(b)
    if op == '=':
        uf.union(a, b)
    elif uf.find(a, b):
        print('yes')
    else:
        print('no')
