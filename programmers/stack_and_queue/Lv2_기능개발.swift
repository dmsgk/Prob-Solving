//
//  Lv2_기능개발.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/26.
//

import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer : [Int] = []
    
    let leftover = progresses.map {100 - $0}
    var leftDays : [Int] = []
    for i in 0..<speeds.count {
        leftDays.append(Int(ceil(Double(leftover[i])/Double(speeds[i]))))
    }
    
    var temp = leftDays[0]
    var cnt = 1
    for idx in 1..<leftDays.count {
        if leftDays[idx] > temp {  // 완성되는 다른 날에 처리가능함
            answer.append(cnt)
            cnt = 1
            temp = leftDays[idx]
        }
        else {
            cnt += 1
        }
        if idx == leftDays.count - 1 {
            answer.append(cnt)
        }
    }
    return answer
}

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])   //     [1, 3, 2]
