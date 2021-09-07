# 찾기
import sys


def get_pi(p):
    m = len(p)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(t, p):
    answer = []
    pi = get_pi(p)
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]

        if t[i] == p[j]:
            if j == len(p) - 1:
                answer.append(i - len(p) + 2)
                j = pi[j]
            else:
                j += 1
    return answer


t = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

answer = kmp(t,p)
print(len(answer))
print(*answer)