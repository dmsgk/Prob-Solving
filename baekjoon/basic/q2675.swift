//
//  q2675.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/05.
//

import Foundation

let t = Int(readLine()!)!

for _ in 0..<t {
    var ansStr = ""
    let arr = readLine()!.components(separatedBy: " ")
    let r = Int(arr[0])!
    let str = arr[1]
    
    
    for char in str {
        for _ in 0..<r {
            ansStr += String(char)
        }
    }
    
    print(ansStr)
    
}
