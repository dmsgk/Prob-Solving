# N과 M (1)
import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())


def permutations(depth, ans):
    if depth == m:
        print(*ans)
        return

    for i in range(1, n+1):
        if i not in ans:
            permutations(depth + 1, ans + [i])


permutations(0, [])