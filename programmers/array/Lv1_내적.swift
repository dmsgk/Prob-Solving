//
//  Lv1_내적.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/23.
//

import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result = 0
    for i in a.indices {
        result += a[i]*b[i]
    }
    return result
}

solution([1,2,3,4], [-3,-1,0,2])
