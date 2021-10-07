# 먹을 것인가 먹힐 것인가
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)

    cnt = 0
    start = 0
    for i in range(n):
        for j in range(start, m):
            if a[i] > b[j]:
                cnt += m-j
                start = j
                break
    print(cnt)