//
//  Lv2_최솟값만들기.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/26.
//

import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    var ans = 0
    let a = A.sorted()
    let b = B.sorted(by: >)
    
    for i in 0..<a.count {
        ans += a[i]*b[i]
    }
    return ans
}
