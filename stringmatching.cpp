// kmp, knuth-morris-pratt, substrings, medium

#include <iostream>
#include <string>
#include <vector>

using namespace std;

string T, P;
vector<int> b;
int n, m;

void kmpPreprocess() {
  int i=0, j=-1;
  b[0] = -1;
  while(i < m) {
    while(j >= 0 && P[i] != P[j]) j = b[j];
    i++; j++;
    b[i] = j;
  }
}

void kmpSearch() {
  bool printed = false;
  int i=0, j=0;
  while(i < n) {
    while(j >= 0 && T[i] != P[j]) j = b[j];
    i++; j++;
    if(j == m) {
      if(printed)
	cout << ' ';
      printed = true;
      cout << i-j;
    }
  }
}

int main() {
  while(getline(cin, P)) {
    getline(cin, T);
    
    b.clear();
    b.reserve(P.size());

    n = T.size();
    m = P.size();
    
    kmpPreprocess();
    kmpSearch();
    
    cout << endl;
  }
  
  return 0;
}
