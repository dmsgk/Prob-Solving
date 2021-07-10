//
//  q1463.cpp
//  cppAlgorithm
//
//  Created by Johyeon Yoon on 2021/07/10.
//
// 1로 만들기
#include <iostream>
using namespace std;

int main() {
    int n, min_num;
    
    cin >> n;
    int *p = new int[n+1];    // int형 변수 [0]
    
    for (int i = 0; i < n+1 ; i++) {
        if (i == 0 or i == 1){
            p[i] = 0;
            continue;
        }
        min_num = n+1;

        if (i % 3 == 0 and i / 3 > 0) {
            min_num = min(min_num, p[i/3]+1);
        }
        if (i % 2 == 0 and i / 2 > 0) {
            min_num = min(min_num, p[i/2]+1);
        }
        min_num = min(min_num, p[i-1]+1);
        p[i] = min_num;
        
    }
    
    cout << p[n];
    delete[] p; 
    return 0;
    
}
