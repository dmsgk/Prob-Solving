# 부분문자열
import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()


def get_pi(p):
    p_len = len(p)
    j = 0
    pi = [0]*p_len
    for i in range(1, p_len):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s, p):
    pi = get_pi(p)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                return 1
            else:
                j += 1
    return 0


print(kmp(s,p))
