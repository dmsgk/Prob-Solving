

def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for A, B, C in fares:
        graph[A-1][B-1] = C
        graph[B-1][A-1] = C

    result = floyd_warshall(graph, n)
    min_cost = result[s-1][a-1] + result[s-1][b-1]
    for k in range(n):
        if s-1 == k:
            continue
        if result[k][a-1] + result[k][b-1] + result[s-1][k] < min_cost:
            min_cost = result[k][a-1] + result[k][b-1] + result[s-1][k]
    return min_cost


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# 14
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
# 18

