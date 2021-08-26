# 멀티탭 스케줄링
import sys
from copy import deepcopy

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))


plugged_in = set()
cnt = 0
for i in range(k):
    # print(plugged_in, li[i], cnt)
    if li[i] in plugged_in:
        continue

    if len(plugged_in) >= n:
        cnt += 1
        out = deepcopy(plugged_in)
        for j in range(i+1, k):
            if len(out) == 1:
                break

            if li[j] in out:
                out.remove(li[j])

        removed_concent = out.pop()
        plugged_in.remove(removed_concent)

    plugged_in.add(li[i])

print(cnt)