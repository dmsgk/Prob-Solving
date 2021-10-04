# 1, 2, 3 더하기 6
import sys

t = int(sys.stdin.readline())
max_num = 0
num_li = []

for _ in range(t):
    n = int(sys.stdin.readline())
    max_num = max(max_num, n)
    num_li.append(n)


dp = [0] * max(6, max_num+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3

for i in range(6, max_num+1):
    dp[i] = dp[i-2] + dp[i-4] + dp[i-6]
    dp[i] %= 1000000009


for num in num_li:
    print(dp[num])
