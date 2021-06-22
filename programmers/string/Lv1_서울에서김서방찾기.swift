//
//  Lv1_서울에서김서방찾기.swift
//  
//
//  Created by Johyeon Yoon on 2021/06/22.
//


func solution(_ seoul:[String]) -> String {
    let idx = seoul.firstIndex(of: "Kim")!
    return "김서방은 \(idx)에 있다"
}

solution(["Jane", "Kim"])
