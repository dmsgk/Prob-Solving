# 용액

import sys

n = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))

result = []
abs_min = sys.maxsize
left, right = 0, n-1
while left < right:
    liq_sum = liq[left] + liq[right]
    if abs(liq_sum) < abs_min:
        result = [liq[left], liq[right]]
        abs_min = abs(liq_sum)
    if liq_sum < 0:
        left += 1
    else:
        right -= 1

print(*result)