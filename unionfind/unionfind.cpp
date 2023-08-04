// union-find, data structure, medium/hard

#include <iostream>
#include <vector>

using namespace std;

class UnionFind{
private:
  vector<int> p, rank;
public:
  UnionFind(int N) {
    rank.resize(N);
    p.resize(N);
    for(int i=0; i<N; i++) {
      p[i] = i;
      rank[i] = 0;
    }
  }
  int findSet(int i) {
    return (p[i] == i) ? i : (p[i] = findSet(p[i]));
  }
  bool isSameSet(int i, int j) {
    return findSet(i) == findSet(j);
  }
  void unionSet(int i, int j) {
    if(!isSameSet(i, j)) {
      int x = findSet(i), y = findSet(j);
      if(rank[x] > rank[y]) {
	p[y] = x;
      }
      else {
	p[x] = y;
	if(rank[x] == rank[y])
	  rank[y]++;
      }
    }
  }
};

int main() {
  int n, q;
  int temp;
  
  temp = scanf("%d %d", &n, &q);
  
  UnionFind uf(n);
  
  for(int i=0; i<q; i++) {
    char op;
    int a, b;
    
    temp = scanf("%c", &op); //consume newline character
    temp = scanf("%c %d %d", &op, &a, &b);
    
    if(op == '=')
      uf.unionSet(a, b);
    else if(uf.isSameSet(a, b))
      cout << "yes\n";
    else
      cout << "no\n";
  }
  
  return 0;
}
