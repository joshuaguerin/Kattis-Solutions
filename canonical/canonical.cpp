// dynamic programming, dp, subset-sum, hard

#include <iostream>
#include <vector>

using namespace std;

// compute greedy version
int greedy(int n, vector<int> cs) {
  int total = 0;
  
  for(int i=cs.size()-1; 0<=i; i--) {
    // Compute directly, a while loop will stall out
    // on bad cases.
    int div = n/cs[i];
    total += div;
    n -= cs[i]*div;

    // Not required, but took runtime from 3.14s to 2.95s
    if(n==0)
      break;
  }
  return total;
}

int main() {
  int n;
  cin >> n;

  // read coin values
  vector<int> cs(n, 0);
  for(int i=0; i<n; i++) {
    cin >> cs[i];
  }

  // create dp array
  int max = cs[cs.size()-1] + cs[cs.size()-2];
  vector<int> memo(max, 0);

  // populate initial values for dp
  for(int i=0; i<cs.size(); i++) {
    memo[cs[i]] = 1;
  }

  // dp up to end point
  for(int i=0; i<max; i++) {
    if(memo[i] != 0) {
      if(memo[i] < greedy(i, cs)) {
	cout << "non-canonical" << endl;
	return 0;
      }

      for(int j=0; j<cs.size(); j++) {
	int c = cs[j];
	if(i+c < memo.size() && (memo[i+c] == 0 || memo[i]+1 < memo[i+c]))
	  memo[i+c] = memo[i]+1;
      }
    }
  }
  cout << "canonical" << endl;
  
  return 0;
}

