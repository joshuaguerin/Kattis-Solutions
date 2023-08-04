// all pairs shortest path, graph, dynamic programming, dp, floyd warshall

#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>

using namespace std;

const int INF=INT_MAX;

// for debugging
void print(vector<vector<int> > AdjMat) {
    for(int i=0; i<AdjMat.size(); i++) {
        for(int j=0; j<AdjMat[i].size(); j++)
            cout << AdjMat[i][j] << " ";
        cout << endl;
    }
}

int main() {
    int n, m, q;
    cin >> n >> m >> q;
    
    bool first=true;
    
    while(n != 0 || m != 0 || q != 0) {
      // create, populate matrix
      vector<vector<int> > AdjMat(n, std::vector<int>(n, INF));

      // diagonals are zero
      for(int i=0; i<AdjMat.size(); i++) {
        AdjMat[i][i] = 0;
      }

      // extra space after first run
      if(first == true)
	first = false;
      else
	cout << endl;

      // populate edges
      for(int i=0; i<m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        
	AdjMat[u][v] = min(AdjMat[u][v], w);
      }

      // standard Floyd-Warshall from CP3e
      for(int k=0; k<n; k++) {
        for(int i=0; i<n; i++) {
	  for(int j=0; j<n; j++) {
	    if(AdjMat[i][k] != INF && AdjMat[k][j] != INF)
	      AdjMat[i][j] = min(AdjMat[i][j], AdjMat[i][k] + AdjMat[k][j]);
	  }
        }
      }

      // handle queries
      for(int i=0; i<q; i++) {
        int u, v;
        cin >> u >> v;
	
	bool negative_cycle = false;
	// Need to handle negative cycles (breaks Floyd-Warshall
	// indicated by a negative on the diagonal
	for(int d=0; d<n; d++) {
	  if(AdjMat[u][d] != INF && AdjMat[d][v] != INF && AdjMat[d][d] < 0) {
	    negative_cycle = true;
	  }
	}

	if(negative_cycle) {
	  cout << "-Infinity" << endl;
	}
        else if(AdjMat[u][v] == INF) {
	  cout << "Impossible" << endl;
        }
        else {
	  cout << AdjMat[u][v] << endl;
        }
      }
      
      cin >> n >> m >> q;
    }
    return 0;
}

