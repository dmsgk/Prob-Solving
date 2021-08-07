//
//  q1003.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/07.
//

// 1003 피보나치 함수

let t = Int(readLine()!)!
var dp = Array(repeating: 0, count: 41)
dp[1] = 1
for _ in 0..<t {
    let n = Int(readLine()!)!
    fibCnt(n)
    if n == 0 {
        print(1,0)
    }
    else if n == 1 {
        print(0,1)
    }
    else {
        print(dp[n-1], dp[n])
    }
}

func fibCnt(_ n: Int) -> Int{
    if n == 0 {
        return 0
    }
    else if n == 1 {
        return 1
    }
    else {
        if dp[n] == 0 {
            dp[n] = fibCnt(n-1) + fibCnt(n-2)
        }
        return dp[n]
    }
}
