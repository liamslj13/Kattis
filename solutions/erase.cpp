#include <iostream>
using namespace std;

int main() {
  int N;
  cin>>N;
  bool broken=false;
  string str1,str2;
  cin>>str1>>str2;
  int len = str1.length();
  if (N % 2 == 0) {
      if (str1 != str2) broken = true;
  } else {
    for (int i=0;i<len;i++) {
      if (str1[i] == str2[i]) {
        broken = true;
        break;
      }
    }
  }
  if (broken) {
      cout<<"Deletion failed";
  } else {
      cout<<"Deletion succeeded";
  }
  return 0;
}
