#include <iostream>
using namespace std;


int solve(int n) {
    return ((n + 5) * 3) - 10;
}

int main() {
    int k;
    cin >> k;
    cout << solve(k);
}