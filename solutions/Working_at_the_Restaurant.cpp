#include <iostream>
using namespace std;

int main() {
    int N, plates;
    string cmnd;
    
    while (true) {
        cin>>N;
        if (N == 0) {
            break;
        }
        
        int p1 = 0, p2 = 0; // piles
        for (int i = 0; i<N;i++) {
            cin>>cmnd>>plates; // get plates
            if (cmnd == "DROP") {
                p2 += plates;
                cout<<"DROP 2 "<<plates<<endl;
            } else {
                if (p1 >= plates) {
                    cout<<"TAKE 1 "<<plates<<endl;
                    p1 -= plates;
                } else {
                    if (p1 != 0) {
                        cout<<"TAKE 1 "<<p1<<endl;
                        plates -= p1;
                    }
                    cout<<"MOVE 2->1 "<<p2<<endl;
                    cout<<"TAKE 1 "<<plates<<endl;              
                    p1 = p2 - plates;
                    p2 = 0;
                }
            }
        }
        cout<<'\n';
    }
}