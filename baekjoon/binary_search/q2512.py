# 예산
import sys


n = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start, end = 1, max(request)
while start <= end:
    mid = (start+end)//2
    total = 0
    for req in request:
        if req > mid:
            req = mid
        total += req
    if total <= m:
        start = mid+1
    else:
        end = mid - 1
print(end)
