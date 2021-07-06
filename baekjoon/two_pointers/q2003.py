# 수들의 합2

import sys

# 입력
n, m = map(int, sys.stdin.readline().strip().split())
num_li = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * (n+1)
for i, num in enumerate(num_li):
    dp[i+1] = dp[i] + num

left, right = 0, 1
cnt = 0

while left <= right and right < n+1:
    if dp[right] - dp[left] > m:
        left += 1
    elif dp[right] - dp[left] < m:
        right += 1
    else:
        cnt += 1
        right += 1

print(cnt)