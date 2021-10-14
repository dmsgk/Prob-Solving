# 동전1
import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]


dp = [0]*(k+1)
dp[0] = 1

for i in coins:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])