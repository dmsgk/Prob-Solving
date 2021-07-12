# 집합의 표현

import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().rstrip().split())

par = [i for i in range(n+1)]   # 0부터 n까지 자기자신을 최상단 노드값으로 갖도록 초기화한 배열 생성


def find(x):  # x의 최상단 노드 찾기
    global par
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    global par
    x, y = find(x), find(y)
    if x == y:
        return
    par[x] = y  # x의 최상단 노드를 y의 최상단 노드로 업데이트하여 union


def solution(c, a, b):
    global par
    if c == 0:
        union(a, b)
    else:
        par_a, par_b = find(a), find(b)
        if par_a == par_b:
            print("YES")
        else:
            print("NO")


for _ in range(m):
    c, a, b = map(int, sys.stdin.readline().rstrip().split())
    solution(c,a,b)
