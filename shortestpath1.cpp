// medium, dijkstra, shortest path

#include <climits>
#include <iostream>
#include <queue>

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;

const int INF = INT_MAX;

int main() {
  int n, m, q, s;
  bool first=true;
  
  cin >> n >> m >> q >> s;
  
  while(n!=0 || m!=0 || q!=0 || s!=0 ) {
    if(first)
      first = false;
    else
      cout << endl;
    
    vector<vector<ii> > AdjList;
    
    AdjList.resize(n, vector<ii>());
  
    for(int i=0; i<m; i++) {
      int u, v, w;
      cin >> u >> v >> w;

      AdjList[u].push_back(make_pair(v, w));
    }


    vi dist(n, INF); dist[s] = 0;
    priority_queue<ii, vector<ii>, greater<ii> > pq; pq.push(ii(0, s));
    vector<bool> reached;
    reached.resize(n, false);
    reached[s] = true;

    // From CP3
    while(!pq.empty()) {
      ii front = pq.top(); pq.pop();
      int d = front.first, u = front.second;
      if(d > dist[u]) continue;
      for(int j=0; j<(int)AdjList[u].size(); j++) {
	ii v = AdjList[u][j];

	reached[v.first] = true;
      
	if(dist[u] + v.second < dist[v.first]) {
	  ii v = AdjList[u][j];
	  if(dist[u] + v.second < dist[v.first]) {
	    dist[v.first] = dist[u] + v.second;
	    pq.push(ii(dist[v.first], v.first));
	  }
	}
      }
    }

    for(int i=0; i<q; i++) {
      int query;
      cin >> query;
      if(reached[query] == true)
	cout << dist[query] << endl;
      else
	cout << "Impossible" << endl;
    }


    cin >> n >> m >> q >> s;
  }

  return 0;
}
