#include <iostream>
using namespace std;
#define fast_io() ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define ll long long
#define ld long double
#define endl "\n"

int solve(int n) {
    if (n == 1)
        return 1;
    int printers = 1;
    int days = 0;
    while (printers < n) {
        printers *= 2;
        days++;
    }
    return days + 1;
}



int main() {
    fast_io();
    int n;
    cin>>n;

    cout<<solve(n);
    return 0;
}