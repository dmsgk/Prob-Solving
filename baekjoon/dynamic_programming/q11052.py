# 카드 구매하기
import sys

n = int(sys.stdin.readline())
pi = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
dp[1] = pi[0]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + pi[j-1])

print(dp[n])
