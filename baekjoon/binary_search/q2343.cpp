//
//  q2343.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/09/02.
//

#include <iostream>
#include <vector>
using namespace std;
int n, m;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> m;
    int sum = 0;
    vector<int> lecture(n);
    for (int i = 0; i < n; i++) {
        cin >> lecture[i];
        sum += lecture[i];
    }
    
    int start, end;
    start = 1;
    end = sum;
    
    while (start <= end) {
        int m_cnt = 0, temp_sum = 0;
        int mid = (start + end ) / 2;
        bool flag = false;
        for (int i = 0; i < n; i++){
            if (lecture[i] > mid) {
                flag = true;
                break;
            }
            
            if (temp_sum + lecture[i] > mid){
                m_cnt += 1;
                temp_sum = 0;
            }
  
            temp_sum += lecture[i];
            if (i == n-1) {
                m_cnt += 1;
            }
        }
        
        if (!flag && m_cnt <= m) {
            end = mid -1;
        }
        else {
            start = mid + 1;
        }
    }
    cout << start;

    return 0;
}
