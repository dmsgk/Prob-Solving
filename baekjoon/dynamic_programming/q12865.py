# 평범한 배낭
import sys

n, k = map(int, sys.stdin.readline().split())
weight, value = [0], [0]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j - weight[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])  # 해당 물품을 넣지않거나 해당 물품을 넣을 경우 중 큰경우
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])