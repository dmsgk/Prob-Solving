//
//  q11050.cpp
//  cppAlgorithm
//
//  Created by Johyeon Yoon on 2021/07/09.
//

#include <iostream>

using namespace std;

int factorial(int num){
    if (num == 0) return 1;
    int result = 1;
    for (int i=num; i > 0; i--){
        result *= i;
    }
    
    return result;
}

int main(){
    int n, k;
    cin >> n >> k;
    
    cout << factorial(n) / (factorial(n-k) * factorial(k));
    
    return 0;
}


