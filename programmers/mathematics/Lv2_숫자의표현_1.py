# in을 찾는 문제를 리스트에서 set으로 변경하여 효율성문제 해결

def solution(n):
    answer = 0
    dp = [1, 1]

    def natural_sum(n):
        for i in range(2, n+1):
            dp.append(dp[i-1]+i)
        return dp[n]
    natural_sum(n)
    dp = set(dp)
    for n_sum in dp:
        if n_sum == n:
            answer += 1
        elif n_sum > n:
            a = n_sum -n
            if a in dp:
                answer += 1
    return answer

print(solution(15))