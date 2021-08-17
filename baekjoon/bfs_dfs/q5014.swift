//
//  q5014.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/17.
//

import Foundation

// F, S, G, U, D
let inputArr = readLine()!.components(separatedBy: " ").map({Int(String($0))!})
let f = inputArr[0]
let s = inputArr[1]
let g = inputArr[2]
let u = inputArr[3]
let d = inputArr[4]

//bfs

func bfs() -> Int {
    var queue : [[Int]] = [[s, 0]] // 현재위치, 버튼수
    var curser = 0
    var visited : Set<Int> = [s]
    while queue.count > curser {
        let q = queue[curser]
        let currFloor = q[0]
        let cnt = q[1]
        
        if currFloor == g {
            return cnt
        }
        
        if currFloor + u <= f && !visited.contains(currFloor + u ){
            queue.append([currFloor + u, cnt + 1])
            visited.insert(currFloor + u)
        }
        
        if currFloor - d >= 1 && !visited.contains(currFloor - d ){
            queue.append([currFloor - d, cnt + 1])
            visited.insert(currFloor - d)
        }
        curser += 1
    }
    return -1
}

let sol = bfs()

if sol == -1 {
    print("use the stairs")
}
else {
    print(sol)
}
