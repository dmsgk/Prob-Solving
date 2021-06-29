# 나무 자르기
# Python3로는 시간초과, PyPy로는 통과하는 코드.
import sys

n, m = map(int, sys.stdin.readline().strip().split())
h_of_trees = list(map(int, sys.stdin.readline().strip().split()))
start, end = 0, max(h_of_trees)


while start <= end:
    mid = (start + end)//2
    sliced_len = 0
    for h in h_of_trees:
        if h - mid > 0:
            sliced_len += h-mid
    if sliced_len < m:  # 잘린 총 길이가 m보다 짧은 경우, 더 낮은 곳에서 잘라야.
        end = mid - 1
    else:  # 잘린 총 길이가 m과 같거나 그보다 긴 경우. 가져갈 수 있는 상태지만 가장 높은 상태를 얻기 위해 start  업데이트.
        start = mid + 1

print(end)