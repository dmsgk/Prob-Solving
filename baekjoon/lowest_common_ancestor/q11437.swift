//
//  q11437.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/16.
//

import Foundation


let n = Int(readLine()!)!
var graph : [[Int]] = Array(repeating: [], count: n+1)
var d : [Int] = Array(repeating: -1, count: n+1)
var par : [Int] = Array(repeating: 0, count: n+1)

for _ in 0..<n-1 {
    let nodes = readLine()!.components(separatedBy: " ").map({ Int($0)! })
    graph[nodes[0]].append(nodes[1])
    graph[nodes[1]].append(nodes[0])
}

func dfs(_ x: Int, _ depth : Int) {
    d[x] = depth
    for y in graph[x] {
        if d[y] != -1 {
            continue
        }
        par[y] = x
        dfs(y, depth+1)
    }
}

func lca(_ a: Int, _ b : Int) -> Int {
    var a = a
    var b = b
    while d[a] != d[b] {
        if d[a] > d[b] {
            a = par[a]
        }
        else {
            b = par[b]
        }
    }
    
    while a != b {
        a = par[a]
        b = par[b]
    }
    return a
}

dfs(1, 0)

let m = Int(readLine()!)!
for _ in 0..<m {
    let arr = readLine()!.components(separatedBy: " ").map({Int($0)!})
    print(lca(arr[0], arr[1]))
}

