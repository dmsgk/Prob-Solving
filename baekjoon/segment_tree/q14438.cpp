//
//  q14438.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/08/31.
//

// 14438 수열과 쿼리 17
#include <iostream>
#define MAX 100002
#define INF 1e9 + 1
using namespace std;

int n, m;
int arr[MAX];
int tree[MAX * 4];

int init_tree(int start, int end, int node) {
    if (start == end){
        return tree[node] = arr[start];
    }
    
    int mid = (start + end) / 2;
    return tree[node] = min(init_tree(start, mid, 2*node), init_tree(mid+1, end, 2*node +1));
}

int query(int start, int end, int node, int left, int right) {
    // start, end = 현재 탐색중인 구간
    // 최솟값을 찾는 구간(고정된 값)
    if (left > end || right < start){
        return INF;
    }
    
    if (left <= start && right >= end){
        return tree[node];
    }
    
    int mid = (start + end) / 2;
    return min(query(start, mid, 2*node, left, right), query(mid+1, end, 2*node+1, left, right));
    
}

int update(int start, int end, int node, int index)
{
    if (start > index || end < index) {
        return tree[node];
    }
    
    if (start == end) {
        return tree[node] = arr[index];
    }
    
    int mid = (start + end) / 2;

    return tree[node] = min(update(start, mid, node * 2, index), update(mid + 1, end, node * 2 + 1, index));
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    for (int i = 1; i < n+1; i++){
        cin >> arr[i];
    }
    
    init_tree(1, n, 1);

    cin >> m;
    for (int j = 0; j < m; j++){
        int q, a, b;
        cin >> q >> a >> b;
        if (q==1){
            arr[a] = b;
            update(1, n, 1, a);
        }
        else {
            cout << query(1, n, 1, a, b) << "\n";
        }
    }
    

    return 0;
}
