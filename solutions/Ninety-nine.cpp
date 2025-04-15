#include <iostream>
using namespace std;

int main() {
    cout<<1<<endl;
    int n = 1;

    while (n != 99) {
        cin>>n;
        if (n <= 91) {
            cout<<n+1<<endl;
            continue;
        }
        if (n == 91) {
            cout<<n+2<<endl;  
            continue;
        } else if (n == 92) {
            cout<<n+1<<endl;
            continue;
        } else {
            if (n == 95) {
                cout<<n+1<<endl;
                continue;
            } else if (n == 94) {
                cout<<n+2<<endl;
                continue;
            }
        }
        cout<<n+(99-n)<<endl;
    }
}