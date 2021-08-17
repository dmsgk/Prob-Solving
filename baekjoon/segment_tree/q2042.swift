//
//  q2042.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/17.
//

// 구간 합 구하기
import Foundation

let nmkArr = readLine()!.components(separatedBy: " ").map({Int(String($0))!})
let n = nmkArr[0]
let m = nmkArr[1]
let k = nmkArr[2]

var tree : [Int] = Array(repeating: 0, count: 4 * n)
var numArr : [Int] = []

for _ in 0..<n {
    numArr.append(Int(readLine()!)!)
}

func initTree(_ start : Int, _ end : Int, _ node : Int) -> Int {
    if start == end {
        tree[node] = numArr[start]
        return tree[node]
    }
    
    let mid = (start + end) / 2
    tree[node] = initTree(start, mid, node * 2) + initTree(mid+1, end, node * 2 + 1)
    return tree[node]
}

func sumOfSegment(_ start: Int, _ end : Int, _ node : Int, _ left : Int, _ right : Int) -> Int{
    // start, end : 시작, 끝 인덱스
    // left, right : 구간 합 구하는 구간
    if right < start || left > end {
        return 0
    }
    if left <= start && right >= end {
        return tree[node]
    }
    
    let mid = (start + end) / 2
    return sumOfSegment(start, mid, node*2, left, right) + sumOfSegment(mid + 1, end, node * 2 + 1 , left, right)
}

func update(_ start: Int, _ end : Int, _ node : Int, _ idx : Int, _ dif : Int) {
    if idx < start || idx > end { return }
    tree[node] += dif
    if start == end { return }
    
    let mid = (start + end) / 2
    update(start, mid, node * 2, idx, dif)
    update(mid + 1, end, node * 2 + 1, idx, dif)
}


initTree(0, n-1, 1)

for _ in 0..<m+k {
    let cmdArr = readLine()!.components(separatedBy: " ").map({Int(String($0))!})
    let b = cmdArr[1]
    let c = cmdArr[2]

    if cmdArr[0] == 1 {
        // update
        let prevNum = numArr[b-1]
        let dif = c - prevNum
        numArr[b-1] = c
        update(0, n-1, 1, b-1, dif)
    }
    
    else {
        // 구간합 구하기
        print(sumOfSegment(0, n-1, 1, b-1, c-1))
    }
    
}
