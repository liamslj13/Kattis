#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int solve(int a, int b) {
    return a - b;
}

int main() {
    int n;
    int k;
    int j;
    cin>>n>>k>>j;

    cout<<solve(j, n + k);    
}