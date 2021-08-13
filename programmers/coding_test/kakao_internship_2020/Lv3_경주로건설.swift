//
//  Lv3_경주로건설.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/13.
//


import Foundation

func solution(_ board:[[Int]]) -> Int {
    let n = board.count
    var visited : [[Int]] = []
    for _ in 0..<n {
        visited.append(Array(repeating: -1, count: n))
    }
    
    let dx = [1, 0, -1, 0]
    let dy = [0, -1, 0, 1]  // 남서북동
    var queue : [[Int]] = []
    
    // 초기값 설정
    visited[0][0] = 0
    for i in [0,3] {
        let nx = dx[i]
        let ny = dy[i]
        
        if board[nx][ny] == 0 {
            visited[nx][ny] = 100
            queue.append([nx, ny, i, 100])  // 행, 열, 방향, 금액
        }
    }
    
    var curser = 0
    while curser < queue.count {
        let q = queue[curser]
        let x = q[0]
        let y = q[1]
        let dir = q[2]
        let cost = q[3]
        curser += 1
        
        if x == n-1 && y == n-1 {
            continue
        }
        
        for j in 0..<4 {
            let nx = x + dx[j]
            let ny = y + dy[j]
            
            if 0 <= nx && nx < n && 0 <= ny && ny < n && board[nx][ny] == 0 {
                var temp = cost + 100
                if j != dir {
                    temp += 500
                }
                
                if visited[nx][ny] == -1 || temp <= visited[nx][ny] {
                    visited[nx][ny] = temp
                    queue.append([nx, ny, j, temp])
                }
            }
        }
    }
    return visited[n-1][n-1]
}


solution([[0,0,0],
          [0,0,0],
          [0,0,0]]) //    900

solution([[0,0,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0,1],
          [0,0,1,0,0,0,1,0],
          [0,1,0,0,0,1,0,0],
          [1,0,0,0,0,0,0,0]]) //    3800

solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]) // 2100
solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]) // 3200

