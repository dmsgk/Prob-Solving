//
//  main.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/04.
//

// q2667 단지번호붙이기
import Foundation


var board : [[Character]] = []
let n = readLine()!
for _ in 0..<Int(n)! {
    let r = readLine()!
    let row = Array(r)
    board.append(row)
}

var numOfDanji = 0
var numOfHouse : [Int] = []


func bfs(_ i : Int, _ j : Int) {
    var idx = 0
    var queue = [[i,j]]
    board[i][j] = "0"
    
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, -1, 1]
    
    var cntHouse = 0
    while idx < queue.count {
        
        let q = queue[idx]
        let x = q[0]
        let y = q[1]
        
        idx += 1
        
        cntHouse += 1
        
        for k in 0..<4 {
            let nx = x + dx[k]
            let ny = y + dy[k]
            
            if 0 <= nx && nx < Int(n)! && 0 <= ny && ny < Int(n)! && board[nx][ny] == "1" {
                queue.append([nx,ny])
                board[nx][ny] = "0"
            }
        }
    }
    numOfHouse.append(cntHouse)
    
}


for i in 0..<Int(n)! {
    for j in 0..<Int(n)! {
        if board[i][j] == "1" {
            numOfDanji += 1
            bfs(i, j)
        }
    }
}


print(numOfDanji)
numOfHouse.sort()
for h in numOfHouse {
    print(h)
}
