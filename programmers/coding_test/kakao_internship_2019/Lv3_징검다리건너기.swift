//
//  Lv3_징검다리건너기.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/12.
//
import Foundation

func solution(_ stones:[Int], _ k:Int) -> Int {
    // 시간이 변수. 이분탐색
    var left = 0
    var right = stones.max()!
    
    while left <= right {
        let mid = (left + right) / 2
        var zeroRocks : [Int] = []  // 0값인 징검다리 길이들을 저장
        
        for (idx, val) in stones.enumerated() {
            if idx == 0 {
                if val <= mid {
                    zeroRocks.append(1)
                }
                continue
            }
            
            if val <= mid {
                if stones[idx-1] <= mid {
                    zeroRocks[zeroRocks.count-1] += 1
                }
                else {
                    zeroRocks.append(1)
                }
            }
        }
        
        if zeroRocks.count == 0 {
            left = mid + 1
            continue
        }
        
        let maxChunk = zeroRocks.max()!
        if maxChunk < k {
            left = mid + 1
            
        }
        else {
            right = mid - 1
        }
    }
    return left
}


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)  // 3
