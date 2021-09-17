# 2*n 타일링

import sys

n = int(sys.stdin.readline())

dp = [0]*(n+2)
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10007

print(dp[n])
