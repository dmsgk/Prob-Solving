//
//  Lv3_디스크컨트롤러.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/12.
//


import Foundation

func solution(_ jobs:[[Int]]) -> Int {
    var time = 0
    var total = 0
    var jobsSort = jobs.sorted(by: {$0[0] == $1[0] ? $0[1] < $1[1] : $0[0] < $1[0] })
    jobsSort.sort(by: {$0[1] == $1[1] ? $0[0] < $1[0] : $0[1] < $1[1]})
    
    while jobsSort.count > 0 {
        for i in 0..<jobsSort.count {
            if jobsSort[i][0] <= time {
                time += jobsSort[i][1]
                total += time - jobsSort[i][0]
                jobsSort.remove(at: i)
                break
            }
            if i == jobsSort.count - 1 {
                time += 1
            }
            
        }
    }
    return total/jobs.count
    
}
solution([[0, 3], [1, 9], [2, 6]]) // 9

