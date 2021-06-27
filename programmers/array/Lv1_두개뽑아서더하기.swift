//
//  Lv1_두개뽑아서더하기.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/27.
//

import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var sumSet : Set<Int> = []
    
    for i in 0..<numbers.count-1 {
        for j in i+1..<numbers.count {
            sumSet.insert(numbers[i]+numbers[j])
        }
    }
    return Array(sumSet).sorted()
}


solution([2,1,3,4,1])
