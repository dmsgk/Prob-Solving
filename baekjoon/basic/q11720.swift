//
//  q11720.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/04.
//
// 11720 숫자의 합
import Foundation


let n = Int(readLine()!)!
let arr = Array(readLine()!)

var ans = 0
for i in 0..<n {
    ans += Int(String(arr[i]))!
}
print(ans)
