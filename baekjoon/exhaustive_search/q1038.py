# 감소하는 수
import sys


sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())


def solution(n):
    cnt = 0
    num = 1
    while 1:
        str_n = str(num)
        flag = True
        if len(str_n) == 1:
            pass
        else:
            for i in range(1, len(str_n)):
                if int(str_n[i]) < int(str_n[i - 1]):
                    continue
                else:
                    start = str_n[:i - 1]
                    mid = str(int(str_n[i - 1]) + 1)
                    end = '0' + str_n[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1


if n >= 1023:
    print(-1)
elif n == 0:
    print(0)
else:
    print(solution(n))