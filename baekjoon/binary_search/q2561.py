# 놀이공원

import sys

n, m = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))


def solution(time, n, m):
    if n <= m:
        return n
    start, end = 0,  60000000000
    while start <= end:
        ride_num = m
        mid = (start + end) // 2
        for t in time:
            ride_num += mid // t

        if ride_num >= n:
            end = mid - 1
        else:
            start = mid + 1
    ans_time = start

    cnt = m
    for i in range(m):
        cnt += (ans_time - 1) // time[i]

    for i in range(m):
        if ans_time % time[i] == 0:
            cnt += 1
        if cnt == n:
            return i+1


print(solution(time, n, m))