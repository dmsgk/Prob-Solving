//
//  q1303.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/08/30.
//

// 1303 전투
#include <iostream>
using namespace std;


int n, m;
string board[101][101];
int visited[101][101];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int cnt;
int w_ans, b_ans;

void dfs(int x,int y, string color){
    visited[x][y] = 1;
    
    for (int i=0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
                
        if (0 <= nx < m && 0 <= ny < n && visited[nx][ny] == 0 and board[nx][ny] == color){
            cnt ++;
            dfs(nx, ny, color);
        }
    }
}


int main() {
    cin >> n >> m;
    
    for(int i=0; i<m; i++){
        string row;
        cin >> row;
        for (int j = 0; j < n; j++){
            board[i][j] = row[j];
        }
    }
    
    for(int i=0; i<m; i++){
        for (int j = 0; j < n; j++){
            if (visited[i][j] == 1){
                continue;
            }
            cnt = 1;
            if (board[i][j] == "B"){
                dfs(i, j, "B");
                b_ans += cnt*cnt;
            }
            else {
                dfs(i,j,"W");
                w_ans += cnt * cnt;
            }
        }
    }
    
    cout << w_ans << " " << b_ans;
}
