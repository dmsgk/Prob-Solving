//
//  q1107.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/08.
//

import Foundation

let strN = readLine()!
let n = Int(strN)!
let m = Int(readLine()!)!
var brokenSet = Set<Int>()
if m > 0 {
    brokenSet = Set(readLine()!.components(separatedBy: " ").map({ (value: String) -> Int in return Int(value)! }))
}
var cnt = abs(n - 100)

func solution(num: String) {
    if num.count >= 6 {
        return
    }
    
    for i in 0..<10 {
        if brokenSet.contains(i) {
            continue
        }
        let orderCount = abs(n - Int(num + String(i))!) + num.count+1
        cnt = min(cnt, orderCount)
        solution(num: num+String(i))
    }
}
solution(num: "")
print(cnt)
