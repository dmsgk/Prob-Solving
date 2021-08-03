//
//  Lv1_부족한금액계산하기.swift
//  
//
//  Created by Johyeon Yoon on 2021/08/03.
//

import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    let totalPrice = price * (count * (count+1)/2)
    
    if money >= totalPrice {
        return 0
    }
    
    return Int64(totalPrice - money)
}

solution(3, 20, 4) //10
