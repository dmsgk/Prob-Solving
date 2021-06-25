//
//  Lv1_음양더하기.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/25.
//

import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var result = 0
    for (idx, num) in absolutes.enumerated() {
        if signs[idx] { // 양수일 경우
            result += num
        }
        else {
            result -= num
        }
    }
    return result
}
