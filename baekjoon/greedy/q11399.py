# ATM
import sys

n = int(sys.stdin.readline())
p_li = list(map(int, sys.stdin.readline().split()))

p_li.sort()
cnt = 0

for i in range(n):
    cnt += p_li[i] * (n-i)
print(cnt)
