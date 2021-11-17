# 날짜 계산
import sys


def solution(e, s, m):
    cnt = 1
    a, b, c = 1,1,1
    while 1:
        if a == e and b == s and c == m:
            return cnt
        a, b, c = (a+1) % 16, (b+1) % 29, (c+1) % 20
        if a == 0:
            a = 1
        if b == 0:
            b = 1
        if c == 0:
            c = 1
        cnt += 1


e, s, m = map(int, sys.stdin.readline().split())
print(solution(e,s,m))