#include <bits/stdc++.h>
using namespace std;

int main() {
	int N,temp,arrowCount=0;
	cin>>N;

	int heights[1000001] = {0};

	for (int i=0;i<N;i++) {
	    cin>>temp;

	    if (heights[temp] == 0) {
	        heights[temp-1]++;
	    } else {
	        heights[temp-1]++;
	        heights[temp]--;
	    }
	}

	for (int j=0;j<1000000;j++) {
	    arrowCount += heights[j];
	}

	cout<<arrowCount;
	return 0;
}
