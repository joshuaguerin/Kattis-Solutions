// primes, sieve, math

#include <bitset>
#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

ll _sieve_size;
bitset<100000000> bs;
vi primes;

// Sieve of Eratosthenes from CP3
void sieve(ll upperbound) {
  _sieve_size = upperbound + 1;
  bs.set();
  bs[0] = bs[1] = 0;

  for(ll i=2; i<= _sieve_size; i++)
    if(bs[i]) {
      for(ll j=i*i; j <= _sieve_size; j += i)
	bs[j] = 0;
      primes.push_back(int(i));
    }
}

// Check the above bit vector
bool isPrime(ll N) {
  if(N <= _sieve_size)
    return bs[N];

  for(int i=0; i<(int)primes.size(); i++)
    if(N%primes[i] == 0)
      return false;
  return true;
}

// compute each value as expected
int main() {
  int n, q, total_primes=0;
  cin >> n >> q;

  sieve(n);

  for(int i=2; i<=n; i++) {
    if(bs[i])
      total_primes++;
  }

  cout << total_primes << endl;
  
  for(int i=0; i<q; i++) {
    int x;
    cin >> x;
    if(bs[x])
      cout << 1 << endl;
    else
      cout << 0 << endl;
  }
}
