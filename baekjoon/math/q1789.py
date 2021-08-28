# 수들의 합
import sys

s = int(sys.stdin.readline())
sum = 0
for i in range(1,4294967295):
    sum += i
    if sum > s:
        print(i-1)
        break

