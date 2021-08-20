# 덩치

import sys

n = int(sys.stdin.readline())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
order = [1]*n

for i in range(n):
    for j in range(i+1, n):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            order[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            order[i] += 1

print(*order)


