#include <bits/stdc++.h>
using namespace std;
#define ll long long

const ll MOD = 1000000007;


vector<ll> multiply(vector<ll> x, vector<ll> y) {
    if (y.size() == 3) {
        ll a = (x[0]*y[0] + x[1]*y[1] + x[2]*y[2]) % MOD;
        ll b = (x[3]*y[0] + x[4]*y[1] + x[5]*y[2]) % MOD;
        return {a, b, 1};
    }
    ll a = (x[0]*y[0] + x[1]*y[3] + x[2]*y[6]) % MOD;
    ll b = (x[0]*y[1] + x[1]*y[4] + x[2]*y[7]) % MOD;
    ll c = (x[0]*y[2] + x[1]*y[5] + x[2]*y[8]) % MOD;
    
    ll d = (x[3]*y[0] + x[4]*y[3] + x[5]*y[6]) % MOD;
    ll e = (x[3]*y[1] + x[4]*y[4] + x[5]*y[7]) % MOD;
    ll f = (x[3]*y[2] + x[4]*y[5] + x[5]*y[8]) % MOD;
    
    ll g = (x[6]*y[0] + x[7]*y[3] + x[8]*y[6]) % MOD;
    ll h = (x[6]*y[1] + x[7]*y[4] + x[8]*y[7]) % MOD;
    ll i = (x[6]*y[2] + x[7]*y[5] + x[8]*y[8]) % MOD;
    
    return {a, b, c, d, e, f, g, h, i};
}

vector<ll> matrixExp(vector<ll> x, ll power) {
    if (power == 1) return x;
    vector<ll> half = matrixExp(x, power / 2);
    vector<ll> result = multiply(half, half);
    if (power % 2 == 1)
        result = multiply(x, result);
    return result;
}


int main() {
    ll N;
    cin>>N;
    if (N==1) {
        cout<<1<<endl;
        return 0;
    }
    if (N==2) {
        cout<<2<<endl;
        return 0;
    }
    //vecotr A for exponentiation, base vector f(2) = [2,1,1]
    vector<ll> A = {1,1,1,1,0,0,0,0,1};
    vector<ll> z = {2,1,1};
    
    cout<<multiply(matrixExp(A,N-2), z)[0] % MOD<<endl;
}