#include <bits/stdc++.h>
using namespace std;
#define ll long long 

int main() {
  // n -> # of friends, k -> # of days until bday, d -> today
  int n,k,d,q; // q -> quarantine start
  cin>>n>>k>>d;
 
  ll cc = 0;
  ll bday = (k + d);
  
  for (int i = 0; i < n; i++) {
    cin>>q;
    if (q + 14 <= bday) {
      cc++;
    }
  }

  cout<<cc<<endl;
  return 0;
}