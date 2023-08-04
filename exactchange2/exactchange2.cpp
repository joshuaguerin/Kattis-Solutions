// dynamic programming, dp, subset-sum minimization

#include <iostream>
#include <vector>

using namespace std;

int main() {
  int cases;
  cin >> cases;

  for(int i=0; i<cases; i++) {
    int p, n;
    cin >> p >> n;
    
    vector<int> denoms(n, 0);
    for(int j=0; j<n; j++) {
      int next;
      cin >> next;
      denoms[j] = next;
    }

    vector<int> memo(1000001, -1);
    memo[0] = 0;

    for(int j=0; j<denoms.size(); j++) {
      int c = denoms[j];

      // Must count backward, or we risk duplicating
      // values that we are creating _this_iteration_.
      // (Will otherwise use coins we don't have.)
      for(int k=p-1; 0 <= k; k--) {
	if(memo[k] == -1)
	  continue;
	if(memo[k+c] == -1 || memo[k]+1 < memo[k+c])
	  memo[k+c] = memo[k]+1;
      }
    }

    int total=p;
    while(memo[total] == -1)
      total += 1;

    cout << total << ' ' << memo[total] << endl;
  }

  
  return 0;
}
