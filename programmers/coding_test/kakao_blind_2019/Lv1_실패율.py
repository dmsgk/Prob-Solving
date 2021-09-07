from collections import Counter
import operator


def solution(N, stages):
    stages.sort()
    couter_dict = dict(Counter(stages))
    failure_rate_dict = {i:0 for i in range(1, N+1)}
    i = 0
    denominator = len(stages)

    while i < len(stages):
        curr_num = stages[i]
        if curr_num > N:
            break
        if i > 0:
            denominator -= couter_dict[stages[i-1]]
        failure_rate_dict[stages[i]] = couter_dict[stages[i]] / denominator
        i += couter_dict[curr_num]
    sorted_dict = sorted(failure_rate_dict.items(), key=operator.itemgetter(1), reverse = True)
    answer = [arr[0] for arr in sorted_dict]
    return answer

# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))   # [4,1,2,3]