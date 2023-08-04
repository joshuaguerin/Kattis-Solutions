// medium, BFS, path, dijkstra, graph

#include <iostream>
#include <queue>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <utility>
#include <climits>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

const int INF = INT_MAX;

int total;                                // total number of nodes seen
unordered_map<string, int> indices;       // maps names to indices
unordered_map<string, int>::iterator it;  // (for debugging)
vector<string> names;                     // maps indices to names
vector<vi> AdjList;
int s, t;
vi p;

void printPath(int u) {
  if (u == s) { printf("%s", names[s].c_str()); return; }
  printPath(p[u]);
  printf(" %s", names[u].c_str());
}

vs split(string line) {
  vs words;
  stringstream ss;
  string temp;

  ss << line;
  ss >> temp;
  while(ss) {
    words.push_back(temp);
    ss >> temp;
  }
  return words;
}

int translate(string node) {
  if(indices.find(node) == indices.end()) {
    indices[node] = total;
    if(names.size() < total+1)
      names.resize(total+1);
    names[total] = node;
    total++;
  }
  return indices[node];
}

int main() {
  int n, fst_i, snd_i;
  string fst, snd, rest;
  
  cin >> n;
  for(int i=0; i<n; i++) {
    // Add next batch of edges
    stringstream connections;
    cin >> fst;

    fst_i = translate(fst);

    // resize if necessary
    if(AdjList.size() < fst_i+1)
      AdjList.resize(fst_i+1, vi());
    
    getline(cin, rest);
    vs temp = split(rest);

    // Add connected edges
    for(int j=0; j<temp.size(); j++) {
      snd_i = translate(temp[j]);
      AdjList[fst_i].push_back(snd_i);

      if(AdjList.size() < snd_i+1)
	AdjList.resize(snd_i+1, vi());
      AdjList[snd_i].push_back(fst_i);
    } 
  }

  // Read start, end
  cin >> fst >> snd;
  s = translate(fst);
  t = translate(snd);

  // Perform BFS (from CP3)
  vi dist(total, INF);
  dist[s] = 0;
  queue<int> q; q.push(s);
  p.resize(total, -1);
  bool found = false;
  
  while(!q.empty()) {
    int u = q.front();
    
    q.pop();
    for(int j=0; j<(int)AdjList[u].size(); j++) {
      int v = AdjList[u][j];
      
      if(dist[v] == INF) {
	dist[v] =  dist[u] + 1;
	p[v] = u;
	q.push(v);
	if(v == t) found = true;
      }
    }
  }

  if(!found) {
    cout << "no route found" << endl;
    return 0;
  }
  
  printPath(t);
  printf("\n");
  
  return 0;
}
