# 가장 긴 증가하는 부분수열 4
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


dp = [[ai] for ai in arr]
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j] + [arr[i]]

max_len = 0
max_idx = -1
for idx, arr in enumerate(dp):
    if max_len < len(arr):
        max_len = len(arr)
        max_idx = idx
print(max_len)
print(*dp[max_idx])
