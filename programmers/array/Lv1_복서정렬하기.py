def solution(weights, head2head):
    answer = []
    n = len(weights)

    for i in range(n):
        win_cnt = 0
        heavyer_cnt = 0
        total_cnt = n
        for j in range(n):
            if head2head[i][j] == 'N':
                total_cnt -= 1
            elif head2head[i][j] == 'W':
                win_cnt += 1
                if weights[j] > weights[i]:
                    heavyer_cnt += 1
        if total_cnt == 0:
            win_rate = 0
        else:
            win_rate = win_cnt / total_cnt
        answer.append([win_rate, heavyer_cnt, weights[i], -(i + 1)])

    answer.sort(reverse=True)
    result = [-answer[i][3] for i in range(n)]

    return result