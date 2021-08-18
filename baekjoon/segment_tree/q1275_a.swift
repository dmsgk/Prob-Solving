//
//  q1275_a.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/18.
//

let nq = readLine()!.split{$0 == " "}.map({Int(String($0))!})
let n = nq[0], q = nq[1]
var tree = Array(repeating: 0, count: n * 4 + 1)
var numArr = readLine()!.split{$0 == " "}.map({Int(String($0))!})



func setTree(_ start : Int, _ end: Int, _ node : Int) -> Int {
    if start == end {
        tree[node] = numArr[start]
        return tree[node]
    }
    
    let mid = (start + end) / 2
    tree[node] = setTree(start, mid, node * 2) + setTree(mid + 1, end, node * 2 + 1)
    return tree[node]
}

func update(_ start: Int, _ end: Int, _ node : Int, _ idx : Int, _ dif : Int) {
    if idx < start || idx > end {
        return
    }
    
    tree[node] += dif
    if start == end {
        return
    }
    let mid = (start + end) / 2
    update(start, mid, 2 * node, idx, dif)
    update(mid+1, end, 2 * node + 1, idx, dif)
    return
}

func getSegmentSum(_ start: Int, _ end: Int, _ left : Int, _ right : Int, _ node : Int) -> Int {
    if right < start || left > end {
        return 0
    }
    
    if left <= start && right >= end {
        return tree[node]
    }
    
    let mid = (start + end) / 2
    return getSegmentSum(start, mid, left, right, 2 * node) + getSegmentSum(mid+1, end, left, right, 2 * node + 1)
}


setTree(0, n-1, 1)

for _ in 0..<q {
    let cmdArr = readLine()!.split{$0 == " "}.map({Int(String($0))!})
    var x = cmdArr[0], y = cmdArr[1]
    let a = cmdArr[2], b = cmdArr[3] // a위치의 수를 b로 바꾸어라
    if y < x {
        swap(&x, &y)
    }
    print(getSegmentSum(0, n-1, x-1, y-1, 1))
    
    let prevNum = numArr[a-1]
    let dif = b - prevNum
    numArr[a-1] = b
    update(0, n-1, 1, a-1, dif)
    
}
