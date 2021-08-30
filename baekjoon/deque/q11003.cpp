//
//  q11003.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/08/30.
//

// 11003
#include <iostream>
#include <deque>
using namespace std;

int n, l, a;
deque<pair<int, int>> q;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> l;
    
    for (int i = 0; i < n; i++){
        cin >> a;
        while (!q.empty()){
            pair<int, int> t = q.back();
            if (t.second >= a) {
                q.pop_back();
            } else break;
        }
        
        q.push_back(make_pair(i, a));
        if (q.front().first <= i - l) {
            q.pop_front();
        }
        
        cout << q.front().second;
        if (i != n-1){
            cout << " ";
        }
    }
    
    return 0;
}
