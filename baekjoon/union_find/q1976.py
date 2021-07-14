# 여행가자

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

par = [i for i in range(n+1)]  # 자기 자신을 최상단 부모 값으로 초기화


def find(x):
    global par
    if par[x] == x:
        return x

    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    par[x] = y


for i in range(0,n):
    row = list(map(int, input().rstrip().split()))
    for j in range(i+1, n):
        if row[j] == 1:
            union(i+1,j+1)
            union(j+1,i+1)


plans = list(map(int, input().rstrip().split()))
for i in range(1, m):
    start, end = plans[i-1], plans[i]
    s, e = find(start), find(end)
    if s != e:
        print("NO")
        break
else:
    print("YES")






