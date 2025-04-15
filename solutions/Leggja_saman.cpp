#include <iostream>
using namespace std;

int solve(int n, int k) {
    return n + k;
}

int main() {
    int n;
    int k;
    cin>>n>>k;
    
    cout<<solve(n, k);
}