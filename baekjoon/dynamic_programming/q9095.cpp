//
//  q9095.cpp
//  cppAlgorithm
//
//  Created by Johyeon Yoon on 2021/07/12.
//

#include <iostream>
using namespace std;


int main(){
    int t, n;
    cin >> t;
    
    int dp[11] = {1,1,2};
    for (int j = 3; j < 11; j ++ ) {
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
    }
    
    for (int i = 0; i < t; i++) {
        cin >> n;
        cout << dp[n] << endl;
    }
}
