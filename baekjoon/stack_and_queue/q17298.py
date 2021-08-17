# 오큰수
import sys

n = int(sys.stdin.readline())
num_li = list(map(int, sys.stdin.readline().split()))

ans = [-1] * n
stack = []
stack.append(0)

for i in range(1, n):
    while stack and num_li[stack[-1]] < num_li[i]:
        ans[stack.pop()] = num_li[i]
    stack.append(i)


print(*ans)

## 10 999999 1000000 999998 1000000 4 4 1000000 -1 1000000 -1