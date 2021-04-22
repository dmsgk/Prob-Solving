# 효율성 점수 0..

def solution(n):
    answer = 0
    natural_sum = [1]
    for i in range(2, n + 1):
        natural_sum.append(natural_sum[-1] + i)

    for n_sum in natural_sum:
        if n_sum == n:
            answer += 1
        elif n_sum > n:
            a = n_sum -n
            if a in natural_sum:
                answer += 1

    return answer


print(solution(15))