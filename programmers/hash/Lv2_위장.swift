//
//  Lv2_위장.swift
//  
//
//  Created by Johyeon Yoon on 2021/08/03.
//

import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var clothesDict = [String:Int]()
    
    for c in clothes {
        if clothesDict[c[1]] != nil {
            clothesDict[c[1]]! += 1
        }
        else {
            clothesDict[c[1]] = 1
        }
    }
    
    var ans = 1
    
    for (_, value) in clothesDict{
        ans *= (value+1)
    }
    
    return ans-1
}


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
