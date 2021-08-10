//
//  Lv1_상호평가.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/10.
//

func solution(_ scores:[[Int]]) -> String {
    var ans = ""
    for (i, arr) in scores.enumerated() {
        var sortedArr :[Int] = []
        var score = 0
        for r in 0..<scores.count {
            score += scores[r][i]
            sortedArr.append(scores[r][i])
        }
        sortedArr.sort()
        if (arr[i] == sortedArr[0] && sortedArr[0] != sortedArr[1]) || (arr[i] == sortedArr[sortedArr.count-1] && sortedArr[sortedArr.count-1] != sortedArr[sortedArr.count-2]) {
            score -= arr[i]
            score /= arr.count-1
        }
        else {
            score /= arr.count
        }
        ans += grade(score)
    }
    return ans
}

func grade(_ score : Int) -> String {
    switch score {
    case ..<50:
        return "F"

    case 50..<70:
        return "D"
    
    case 70..<80:
        return "C"
        
    case 80..<90:
        return "B"
    
    default:
        return "A"
    }
}

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]) // "FBABD"

solution([[75, 50, 100], [75, 100, 20], [100, 100, 20]]) // "BBF"
