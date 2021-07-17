# 정수삼각형

import sys
input = sys.stdin.readline


n = int(input())
triangle = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0] * (i+1) for i in range(n)]
for i in range(n):
    if i == 0:
        dp[0] = triangle[0]
    else:
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))
