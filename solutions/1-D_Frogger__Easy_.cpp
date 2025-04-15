#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
    // set board bounds, start point, magic num
    int n, s, m, temp;
    cin>>n>>s>>m;
    
    vector<int> board;
    unordered_map<int, int> seen;
    for (int i = 0; i < n; i++) {
        cin>>temp;
        board.push_back(temp);
    }
    
    int initialIndex = s - 1;
    int currentIndex = initialIndex;
    int i = 0;
    // Game loop
    while (true) {
        int currentValue = board[currentIndex];
        if (currentValue == m) {
            cout<<"magic"<<endl;
            cout<<i<<endl;
            break;
        } else if (currentIndex > n-1) {
            cout<<"right"<<endl;
            cout<<i<<endl;
            break;
        } else if (currentIndex < 0) {
            cout<<"left"<<endl;
            cout<<i<<endl;
            break;
        } else if (seen.find(currentIndex) != seen.end()) {
            cout<<"cycle"<<endl;
            cout<<i<<endl;
            break;
        }
        seen[currentIndex] = 1;
        currentIndex += currentValue;
        i++;
    }
    
    return 0;
}