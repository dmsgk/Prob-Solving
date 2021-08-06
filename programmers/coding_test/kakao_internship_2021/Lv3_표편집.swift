//
//  Lv3_표편집.swift
//  Algorithm_Swift
//
//  Created by Johyeon Yoon on 2021/08/06.
//

import Foundation

func solution(_ n:Int, _ k:Int, _ cmd:[String]) -> String {
    var deletedArr : [[Int]] = []
    var curser : Int = k
    
    var linked = [Int: Int]()
    for i in 0..<n-1 {
        linked[i] = i+1 // 내려가는 방향은 key가 양수이도록
        linked[-i-1] = i // 올라가는 방향은 key가 음수이도록
    }
    
    for c in cmd {
        if c.starts(with: "D") || c.starts(with: "U") {
            let cmdArr = c.components(separatedBy: " ")
            let num = Int(String(cmdArr[1]))!
            
            if c.starts(with: "D"){
                for _ in 0..<num {
                    curser = linked[curser]!
                }
            }
            else {
                for _ in 0..<num {
                    curser = linked[-curser]!
                }
            }
        }
        else if c.starts(with: "C") {
            if let nextNum = linked[curser] { // 다음 수가 있는 경우
                if curser == 0 {
                    linked[-nextNum] = nil
                }
                else {
                    if let prevNum = linked[-curser]{
                        linked[prevNum] = nextNum
                        linked[-nextNum] = prevNum
                        linked[-curser] = nil
                    }
                    else { // 앞의 수가 없을 때
                        linked[-nextNum] = nil
                    }
                }
                linked[curser] = nil
                deletedArr.append([curser, nextNum])
                
                curser = nextNum
            }
            
            else { // 다음 수가 없는 경우
                let prevNum = linked[-curser]!
                linked[-curser] = nil
                linked[prevNum] = nil
                deletedArr.append([curser, prevNum])
                
                curser = prevNum
            }
        }
        else {
            let cmdArr = deletedArr.popLast()!
            let cNum = cmdArr[0]

            // 맨 밑에 표 지운경우 curser , prevNum
            if cmdArr[0] > cmdArr[1] {
                let pNum = cmdArr[1]
                linked[pNum] = cNum
                linked[-cNum] = pNum
            }
            else {
                let nNum = cmdArr[1]
                if let pNum = linked[-nNum] {
                    linked[pNum] = cNum
                    linked[-cNum] = pNum
                    
                }
                linked[cNum] = nNum
                linked[-nNum] = cNum
            }
        }
    }
    
    let numSet = Set(linked.values).union(Set(linked.keys))
    var ans = ""
    
    for i in 0..<n {
        
        if !numSet.contains(i) && !numSet.contains(-i){
            ans += "X"
        }
        else {
            ans += "O"
        }
    }
    return ans
}

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])  // "OOOOXOOO"
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]) // "OOXOXOOO"
solution(4,0,["C", "D 1", "C"])
