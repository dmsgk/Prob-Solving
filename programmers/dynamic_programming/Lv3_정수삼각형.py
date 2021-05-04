def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i+1) for i in range(n)]

    for i in range(n):
        if i == 0:
            dp[0] = triangle[0]
        else:
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            for j in range(1, i):
                dp[i][j]= max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[n-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))