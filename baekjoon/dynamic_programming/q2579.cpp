//
//  q2579.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/08/30.
//

// 2579 계단오르기
#include <iostream>
using namespace std;

int n;
int stair[301];
int dp[301];


int main(){
    cin >> n;
    for (int i = 1; i < n+1; i++){
        cin >> stair[i];
    }
    
    dp[1] = stair[1];
    dp[2] = stair[1]+stair[2];
    dp[3] = max(stair[1]+stair[3],stair[2]+stair[3]);
    
    
    for (int j = 4; j < n+1; j++) {
        dp[j] = max(dp[j-2] + stair[j], dp[j-3]+ stair[j-1] + stair[j]);
    }
    
    cout << dp[n];
    
    
    return 0;
}

