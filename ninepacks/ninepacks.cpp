// dynamic programming, dp, subset sum, knapsack

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
  int d, h, sumd=0, sumh=0;
  cin >> d;

  // read dog packs
  vector<int> dpacks(d);
  for(int i=0; i<d; i++) {
    int temp;
    cin >> temp;
    dpacks[i] = temp;
    sumd += temp;
  } 

  // read bun packs (don't know why I called it h)
  cin >> h;
  vector<int> hpacks(h);
  for(int i=0; i<h; i++) {
    int temp;
    cin >> temp;
    hpacks[i] = temp;
    sumh += temp;
  }
  
  // min sum is the largest possible number
  vector<int> memod((sumd < sumh ? sumd+1 : sumh+1), -1);
  vector<int> memoh((sumd < sumh ? sumd+1 : sumh+1), -1);

  // base condition of no dogs/buns
  memod[0] = 0;
  memoh[0] = 0;

  // dp dogs
  for(int i=0; i<dpacks.size(); i++) {
    int d = dpacks[i];

    //go backwards to avoid accidental duplicates
    for(int j=memod.size()-1; 0<=j; j--) {
      if(memod[j] != -1 && j+d < memod.size() && 
	 (memod[j+d] == -1 || memod[j]+1 < memod[j+d])) {
	memod[j+d] = memod[j] + 1;
      }
    }
  }
  
  // dp buns
  for(int i=0; i<hpacks.size(); i++) {
    int h = hpacks[i];

    // same
    for(int j=memoh.size()-1; 0<=j; j--) {
      if(memoh[j] != -1 && j+h < memoh.size() &&
	 (memoh[j+h] == -1 || memoh[j]+1 < memoh[j+h])) {
	memoh[j+h] = memoh[j] + 1;
      }
    }
  }

  // scan _entire_arrays_ for best value
  int solution = INT_MAX;
  for(int i=0; i<memod.size() && i<memoh.size(); i++) {
    if(0 < memod[i] && 0 < memoh[i]) {
      if(memod[i]+memoh[i] < solution)
	solution = memod[i] + memoh[i];
    }
  }

  // print solution
  if(solution == INT_MAX)
    cout << "impossible" << endl;
  else
    cout << solution << endl;
  
  return 0;
}

