# 이친수
import sys

n = int(sys.stdin.readline())


dp = [[0]*2 for _ in range(91)]
dp[1][1] = 1
dp[2][0] = 1

for i in range(3, 91):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))