# 가장 긴 증가하는 부분 수열 2
import sys
import bisect

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
lis = []
for a in arr:
    if not lis:
        cnt += 1
        lis.append(a)
    else:
        if lis[-1] < a:
            lis.append(a)
            cnt += 1
        else:
            idx = bisect.bisect_left(lis, a)
            lis[idx] = a
print(cnt)
