#include <bits/stdc++.h>
using namespace std;

// dfs?
void printRecursively(vector<vector<int>> &nums, vector<string> &strs, int a) {
    // print string at current node
    cout<<strs[a];
    for (int i : nums[a]) {
        printRecursively(nums, strs, i);
    }
}

int main() {
    // fast io
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // declare variables, idx a and b, last will be the last seen a
    // declare a strings vector init to len(N), nums will be a 2d
    // int vector which will act like a tree
    int N, a, b, last = 0;
    cin>>N;
    vector<string> strs(N);
    vector<vector<int>> nums;
    
    for (int i = 0; i < N; i++) {
        cin>>strs[i];
    }
    
    nums.assign(N, vector<int>());
    for (int j = 0; j < N-1; j++) {
        cin>>a>>b;
        a--; b--;
        nums[a].emplace_back(b);
        last = a;
    }
    
    printRecursively(nums, strs, last);
    return 0;
}