//
//  q1074.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/07.
//

import Foundation

let inputArr = readLine()!.components(separatedBy: " ").map({ (value: String) -> Int in return Int(value)! })

var ans = 0

func recursion(_ n : Int, _ r : Int, _ c : Int, _ ans: inout Int) -> Int {
    if n == 0 {
        return ans
    }
    // 1구간
    if r < Int(pow(Double(2), Double(n-1))) &&  c < Int(pow(Double(2), Double(n-1))) {
        return recursion(n-1, r, c, &ans)
    }
    // 2구간
    else if r < Int(pow(Double(2), Double(n-1))) &&  c >= Int(pow(Double(2), Double(n-1))) {
        ans += Int(pow(Double(2), Double(2*n-2)))
        return recursion(n-1, r, c-Int(pow(Double(2), Double(n-1))), &ans)
    }
    // 3구간
    else if r >= Int(pow(Double(2), Double(n-1))) && c < Int(pow(Double(2), Double(n-1))) {
        ans += 2*Int(pow(Double(2), Double(2*n-2)))
        return recursion(n-1, r-Int(pow(Double(2), Double(n-1))), c, &ans)
    }
    // 4구간
    else {
        ans += 3*Int(pow(Double(2), Double(2*n-2)))
        return recursion(n-1, r-Int(pow(Double(2), Double(n-1))), c-Int(pow(Double(2), Double(n-1))), &ans)
    }
    
}

let n = inputArr[0]
let r = inputArr[1]
let c = inputArr[2]
print(recursion(n,r,c, &ans))
