//
//  q2577.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/04.
//

import Foundation

let a = Int(readLine()!)!
let b = Int(readLine()!)!
let c = Int(readLine()!)!

let num = a * b * c
var strArr = Array(String(num))
strArr.sort()


var ans = Array(repeating: 0, count: 10)
for i in 0..<10 {
    for j in 0..<strArr.count {
        if i != Int(String(strArr[j]))! {
            if i < Int(String(strArr[j]))! {
                break
            }
        }
        else {
            ans[i] += 1
        }
    }
}

for a in ans {
    print(a)
}
