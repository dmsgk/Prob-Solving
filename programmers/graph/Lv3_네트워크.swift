//
//  Lv3_네트워크.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/04.
//

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var visited: [Bool] = Array(repeating: false, count: n)
    var cnt: Int = 0

    func dfs(_ rowIdx: Int) {
        visited[rowIdx] = true
        for i in 0..<n {
            if computers[rowIdx][i] == 1 && visited[i] == false {
                dfs(i)
            }
        }
    }

    for i in 0..<n {
        if !visited[i] {
            cnt += 1
            dfs(i)
        }
    }

    return cnt
}
