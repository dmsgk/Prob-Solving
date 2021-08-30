//
//  q15486.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/08/30.
//

#include <iostream>
#define MAX 1500001
using namespace std;
int n;
int t[MAX], p[MAX];
long long dp[MAX];


int main(){
    cin >> n;
    for (int i = 1; i < n+1; i++){
        cin >> t[i] >> p[i];
    }
    
    for (int j = 1; j < n+1; j ++) {
        dp[j + t[j]] = max(dp[j + t[j]], dp[j] + p[j]);
        dp[j+1] = max(dp[j], dp[j+1]);
    }
    
    cout << dp[n+1];
    return 0;
}
