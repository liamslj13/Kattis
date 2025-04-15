#include <iostream>
using namespace std;

string solve(int n, int k) {
    if (n > k) {
        return "MAGA!";
    } else if (n < k) {
        return "FAKE NEWS!";
    }
    return "WORLD WAR 3!";
} 


int main() {
    int n;
    int k;
    
    cin>>n>>k;
    cout<<solve(n, k);
}