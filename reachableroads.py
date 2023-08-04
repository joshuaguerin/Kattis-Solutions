# union_find, graphs, easy

# CP3 implementation
class union_find:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*(n)
    def _find(self, i):
        self.p[i] =  i if self.p[i]==i else self._find(self.p[i])
        return self.p[i]
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


n = int(input())

for i in range(n):
    m = int(input())
    r = int(input())

    uf = union_find(m)

    # union everything
    for j in range(r):
        (x, y) = list(map(int, input().split()))
        uf.union(x, y)

    # count the number of disjoint sets by repeated find/union
    count = 0
    for j in range(len(uf.p)):
        if(not uf.find(0, j)):
            uf.union(0, j)
            count += 1

    # done
    print(count)

    
