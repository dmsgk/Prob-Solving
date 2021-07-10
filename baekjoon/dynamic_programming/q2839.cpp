//
//  q2839.cpp
//  cppAlgorithm
//
//  Created by Johyeon Yoon on 2021/07/10.
//

#include <iostream>
using namespace std;


int main() {
    int n, quo, rem;
    cin >> n;
    quo = n / 5;
    rem = n % 5;
    
    if (rem==0) {
        cout << quo;
    }
    else if (rem == 1) {
        if (quo > 0) {
            cout << quo + 1;
        }
        else {
            cout << -1;
        }
        
    }
    else if (rem == 2) {
        if (quo >= 2) {
            cout << quo + 2;
        }
        else {
            cout << -1;
        }
    }
    else if (rem == 3) {
        cout << quo + 1;
    }
    else {
        if (quo > 0) {
            cout << quo + 2;
        }
        else {
            cout << -1;
        }
    }
    return 0;
}


