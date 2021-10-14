# 동전2
import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]


dp = [sys.maxsize]*(k+1)
dp[0] = 0

for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] = min(dp[j-i]+1, dp[j])
if dp[k] < sys.maxsize:
    print(dp[k])
else:
    print(-1)