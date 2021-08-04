//
//  Lv2_타겟넘버.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/04.
//

// 타겟넘버
// dfs로 풀이

import Foundation

func dfs(_ number: [Int], _ depth: Int, _ target: Int, _ value: Int, answer: inout Int) {

    if depth >= number.count {
        if target == value { answer = answer + 1 }
        return
    }

    dfs(number, depth + 1, target, value + number[depth], answer: &answer)
    dfs(number, depth + 1, target, value - number[depth], answer: &answer)

}

func solution(_ numbers:[Int], _ target:Int) -> Int {

    var answer = 0
    dfs(numbers, 0, target, 0, answer: &answer)

    return answer
}


print(solution([1, 1, 1, 1, 1], 3)) //5
