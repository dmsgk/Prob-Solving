//
//  q2110.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/09/02.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, c;
vector<int> house;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> c;
    for (int i =0; i < n; i++){
        int temp;
        cin >> temp;
        house.push_back(temp);
    }
    sort(house.begin(), house.end());
    
    int left = 1, right = house[n-1] - house[0];
    while (left <= right) {
        int mid = (left + right) / 2;
        int prev = house[0];
        int c_cnt = 1;
        
        for (int j = 1; j < n; j++) {
            if ((house[j] - prev) >= mid){
                c_cnt ++;
                prev = house[j];
            }
        }
        if (c_cnt >= c) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    cout << right;
    return 0;
}
