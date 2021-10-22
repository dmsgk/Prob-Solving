//
//  Lv2_타겟넘버.cpp
//  AlgorithmCpp
//
//  Created by Johyeon Yoon on 2021/10/22.
//

#include <string>
#include <vector>
#include <iostream>
using namespace std;


void dfs(vector<int> &numbers, int depth, int curr_sum, int &target, int &answer) {
    if (depth >= numbers.size()) {
        if (curr_sum == target) {
            answer ++;
        }
        return;
    }
    dfs(numbers, depth + 1, curr_sum + numbers[depth], target, answer);
    dfs(numbers, depth + 1, curr_sum - numbers[depth], target, answer);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    dfs(numbers, 0, 0, target, answer);
    return answer;
}
