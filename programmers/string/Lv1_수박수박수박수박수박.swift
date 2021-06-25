//
//  Lv1_수박수박수박수박수박수? .swift
//  
//
//  Created by Johyeon Yoon on 2021/06/25.
//

func solution(_ n:Int) -> String {
    var result = ""
    let cnt = n / 2
    if cnt>0 {
        for _ in 1...cnt {
            result += "수박"
        }
    }
    if n % 2 == 1 {
        result += "수"
    }
    return result
}

solution(1)

