// mst, graph algorithms, kruskal, minimum spanning tree

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;

// from CP3
class union_find {
private:
  vector<int> p, rank;
public:
  union_find(int n) {
    rank.assign(n, 0);
    p.assign(n, 0);
    for(int i=0; i<n; i++)
      p[i] = i;
  }
  int findSet(int i) {
    while(p[i] != i) {
      p[i] = p[p[i]];
      i = p[i];
    }
    return i;
  }
  int find(int i, int j) {
    return findSet(i) == findSet(j);
  }
  void unionSet(int i, int j) {
    int ii = findSet(i), jj = findSet(j);
    if(ii == jj)
      return;
    if(rank[ii] > rank[jj])
      p[jj] = ii;
    else {
      p[ii] = jj;
      if(rank[ii] == rank[jj])
	rank[jj]+=1;
    }
  }
};


int main() {
  int n, m, u, v, w;

  cin >> n >> m;

  // modified from CP3
  while(n || m) {
    vector< pair<int, ii> > EdgeList;
    vector<ii> MST;
    for(int i=0; i<m; i++) {
      cin >> u >> v >> w;

      EdgeList.push_back(make_pair(w, ii(u, v)));
    }
    sort(EdgeList.begin(), EdgeList.end());

    int mst_cost = 0;
    union_find UF(n);

    for(int i=0; i<m; i++) {
      pair<int, ii> front = EdgeList[i];
      if(!UF.find(front.second.first, front.second.second)) {
	mst_cost += front.first;

	// modification: added edge list
	// (preserves order requested in problem)
	if(front.second.first < front.second.second)
	  MST.push_back(front.second);
	else
	  MST.push_back(make_pair(front.second.second, front.second.first));
	UF.unionSet(front.second.first, front.second.second);
      }
    }

    // Modification: error checking in tree construction
    // MST.size() tells whether tree is complete
    if(MST.size() == n-1) {
      cout << mst_cost << endl;
      sort(MST.begin(), MST.end());
      for(int i=0; i<MST.size(); i++)
	cout << MST[i].first << ' ' << MST[i].second << endl;
    }
    else
      cout << "Impossible" << endl;

    cin >> n >> m;
  }
  
  return 0;
}
