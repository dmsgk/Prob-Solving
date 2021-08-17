//
//  q11659.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/17.
//

import Foundation

let nmArr = readLine()!.components(separatedBy: " ").map({Int(String($0))!})
let n = nmArr[0]
let m = nmArr[1]

let numArr = readLine()!.components(separatedBy: " ").map({Int(String($0))!})
var dp = Array(repeating: 0, count: n+1) // dp 배열

for i in 0..<n {
    dp[i+1] = dp[i] + numArr[i]
}


for _ in 0..<m {
    let ijArr = readLine()!.components(separatedBy: " ").map({Int(String($0))!})
    let i = ijArr[0]
    let j = ijArr[1]
    print(dp[j]-dp[i-1])
}
