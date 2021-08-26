# N과 M (3)
import sys

sys.setrecursionlimit(10**9)
n, m = map(int, sys.stdin.readline().split())


def recursion(depth, ans):
    if depth == m+1:
        print(*ans)
        return

    for i in range(1, n+1):
        recursion(depth + 1, ans+[i])


recursion(1, [])