//
//  Lv1_K번째수.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/23.
//

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var result: [Int] = []
    for c in commands {
        let i = c[0]
        let j = c[1]
        let k = c[2]
        
        var slicedArr = Array(array[i-1...j-1])
        slicedArr.sort()
        result.append(slicedArr[k-1])

    }
    return result
}


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
