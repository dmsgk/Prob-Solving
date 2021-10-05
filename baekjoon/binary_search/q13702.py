# 이상한 술집
import sys

n, k = map(int, sys.stdin.readline().split())
cap_li = [int(sys.stdin.readline()) for _ in range(n)]


start, end = 0, max(cap_li)
if start == end:
    print(0)
else:
    while start <= end:
        cnt = 0
        mid = (start+end)//2
        for cap in cap_li:
            if cap > 0:
                cnt += cap // mid

        if cnt >= k:
            start = mid + 1
        else:
            end = mid - 1
    print(end)