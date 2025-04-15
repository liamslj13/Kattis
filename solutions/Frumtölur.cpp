// could try sieve of eratosthenes but no too complicated
// 100 is small, use brute force
#include <iostream>
using namespace std;

int main() {
    cout<<2<<endl;
    for (int i = 3; i < 10; i++) {
        if (i == 9) {
            continue;  
        } else if (i < 10 && i % 2 != 0) {
            cout<<i<<endl;
        } else if (i % 2 == 0) {
            continue;
        }
    } for (int j = 11; j < 100; j++) {
        if (j % 2 == 0|| j % 3 == 0 || j % 5 == 0 || j % 7 == 0 || j % 9 == 0) {
            continue;
        }

        cout<<j<<endl;
    }   
    
    return 0;
}