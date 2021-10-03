# 1, 2, 3 더하기 3
import sys

t = int(sys.stdin.readline())
num_li = []
for _ in range(t):
    n = int(sys.stdin.readline())
    num_li.append(n)

max_num = max(num_li)
dp = [0] * (max_num+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max_num+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= 1000000009

for num in num_li:
    print(dp[num])
