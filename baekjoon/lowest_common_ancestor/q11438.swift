//
//  q11438.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/16.
//

import Foundation


final class FileIO {
    private let buffer:[UInt8]
    private var index: Int = 0

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        
        buffer = Array(try! fileHandle.readToEnd()!)+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }

        return buffer[index]
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true

        while now == 10
                || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45 { isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1:-1)
    }

    @inline(__always) func readString() -> String {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return String(bytes: Array(buffer[beginIndex..<(index-1)]), encoding: .ascii)!
    }

    @inline(__always) func readByteSequenceWithoutSpaceAndLineFeed() -> [UInt8] {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return Array(buffer[beginIndex..<(index-1)])
    }
}

let file = FileIO()

let n = file.readInt()
var graph : [[Int]] = Array(repeating: [], count: n+1)
var d : [Int] = Array(repeating: -1, count: n+1)
var par : [[Int]] = Array(repeating: Array(repeating: 0, count: 21), count: n+1)

for _ in 0..<n-1 {
    let nodes = [file.readInt(), file.readInt()]
    graph[nodes[0]].append(nodes[1])
    graph[nodes[1]].append(nodes[0])
}

func dfs(_ x: Int, _ depth : Int) {
    d[x] = depth
    for y in graph[x] {
        if d[y] != -1 {
            continue
        }
        par[y][0] = x
        dfs(y, depth+1)
    }
}

func setParent() {
    dfs(1, 0)
    for i in 1..<21 {
        for j in 1..<n+1 {
            par[j][i] = par[par[j][i-1]][i-1]
        }
    }
}

func lca(_ a: inout Int, _ b : inout Int) -> Int {
    if d[a] != d[b]{
        if d[a] > d[b] {
            swap(&a, &b)
        }
    
        for i in stride(from: 20, through: 0, by: -1) {
            if d[b] - d[a] >= (1<<i) {
                b = par[b][i]
            }
        }
    }
    
    if a == b {
        return a
    }
    
    if b != a {
        for i in stride(from: 20, through: 0, by: -1) {
            if par[a][i] != par[b][i] {
                a = par[a][i]
                b = par[b][i]
            }
        }
    }

    return par[a][0]
}

setParent()

let m = file.readInt()
for _ in 0..<m {
    let arr = [file.readInt(), file.readInt()]
    var a = arr[0]
    var b = arr[1]
    print(lca(&a, &b))
}

