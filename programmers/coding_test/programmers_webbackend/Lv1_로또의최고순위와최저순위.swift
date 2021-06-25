//
//  Lv1_로또의최고순위와최저순위.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/25.
//

import Foundation

func solution(_ lottos:[Int], _ win_nums: [Int]) -> [Int] {
    var answer : [Int] = [0, 0]   // 최고등수, 최저등수
    let orderDict = [6 : 1, 5 : 2, 4 : 3, 3: 4, 2 : 5, 1 : 6, 0 : 6]  // 맞힌 개수가 key, 등수가 value
    let certainNum = lottos.filter {$0 > 0}
    let leftoverWinNums = Set(win_nums).subtracting(Set(certainNum))
    let equalNums = 6 - leftoverWinNums.count   // 당첨번호와 일치하는 숫자 수
    answer[1] = orderDict[equalNums]!
    let maxNums = equalNums + min(leftoverWinNums.count, 6 - certainNum.count)
    answer[0] = orderDict[maxNums]!
  
    return answer
}


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
