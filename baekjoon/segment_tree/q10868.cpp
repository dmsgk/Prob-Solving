//
//  q10868.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/08/31.
//

// 10868 최솟값
#include <iostream>
#define MAX 100002
#define INF 1e9+1
using namespace std;

int n, m;
int arr[MAX];
long long tree[4 * MAX];

long long init_tree(int left, int right, int node){
    if (left == right) {
        return tree[node] = arr[left];
    }
    
    int mid = (left + right) / 2;
    return tree[node] = min(init_tree(left, mid, 2*node), init_tree(mid+1, right, 2*node+1));
    
}

long long query(int start, int end, int node, int left, int right){
    // start, end : 시작, 끝 인덱스
    // left, right : 최소값 구하는 구간
    if (left > end || right < start){
        return INF;
    }
    
    if (left <= start && right >= end){
        return tree[node];
    }
    
    int mid = (start + end) / 2;
    
    return min(query(start, mid, 2 * node, left, right), query(mid+1, end, 2 * node+1, left, right));
    
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> m;
    
    for (int i = 1; i < n+1; i++){
        cin >> arr[i];
    }
    
    init_tree(1, n, 1);
    
    for (int j = 0; j < m; j++){
        int a, b;
        cin >> a >> b;
        if (a > b) swap(b,a);
        cout << query(1, n, 1, a, b) << "\n";
        
    }
    
    return 0;
}
