# 케빈베이컨의 6단계법칙
import sys


def floyd_warshall(graph, n):
    result = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if result[i][j] > result[i][k] + result[k][j]:
                    result[i][j] = result[i][k] + result[k][j]
    return result


n, m = map(int, sys.stdin.readline().split())
graph = [[n]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for r in range(n):
    graph[r][r] = 0

result = floyd_warshall(graph, n)
answer = []

for x in range(n):
    x_kb = sum(result[x])
    answer.append((x+1, x_kb))


answer.sort(key=lambda i : (i[1], i[0]))
print(answer[0][0])