/*
// Two pointers did not work, perhaps I wrote the solution wrong
#include <bits/stdc++.h>
using namespace std;


// Try an approach such as two sum
bool solve(vector<int> b, int target) {
    // Take vector calculate difference, check dictionary of seen for said difference 
    unordered_map<int, int> seen;
    
    for (int i = 0; i < b.size(); i++) {
        int d = target - b[i];
        if (seen.find(d) != seen.end()) {
            cout<<d<<" "<<b[i]<<endl;
            return true;
        } else {
            seen[b[i]] = i;
        }
    }

    return 0;
}


int main() {
    int nb, target, temp;
    vector<int> bags;
    
    cin>>nb>>target;
    
    for (int i = 0; i < nb; i++) {
        cin>>temp;
        bags.push_back(temp);
    }
    
    if (!solve(bags, target)) {
        cout<<"Neibb"<<endl;
    }
} */

#include <bits/stdc++.h>
using namespace std;

#define ll long long

// Try an approach such as two sum
bool solve(vector<ll> b, ll target) {
    // Take vector calculate difference, check dictionary of seen for said difference 
    unordered_map<ll, ll> seen;
    
    for (int i = 0; i < b.size(); i++) {
        ll d = target - b[i];
        if (seen.find(d) != seen.end()) {
            cout<<d<<" "<<b[i]<<endl;
            return true;
        } else {
            seen[b[i]] = i;
        }
    }

    return 0;
}


int main() {
    ll nb, target, temp;
    vector<ll> bags;
    
    cin>>nb>>target;
    
    for (int i = 0; i < nb; i++) {
        cin>>temp;
        bags.push_back(temp);
    }
    
    if (!solve(bags, target)) {
        cout<<"Neibb"<<endl;
    }
}

