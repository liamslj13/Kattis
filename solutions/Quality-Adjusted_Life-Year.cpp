#include <iostream>
using namespace std;


int main() {
  float qaly = 0;
  float q,y;
  int N;
  cin>>N;
  for (int i = 0; i<N;i++) {
    cin>>q>>y;
    qaly += q*y;
  }

  cout<<qaly<<endl;
  return 0;
}