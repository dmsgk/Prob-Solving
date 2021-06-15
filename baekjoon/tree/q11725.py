import sys
sys.setrecursionlimit(10**9)


n = int(sys.stdin.readline().strip())
linked_list = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().strip().split())
    linked_list[x].append(y)
    linked_list[y].append(x)
parents = [0]*(n+1)
parents[1] = 1
stack = [1]

def dfs(parents, stack):
    visited = set()
    while stack:
        start = stack.pop()
        visited.add(start)
        children = linked_list[start]
        for c in children:
            if c not in visited:
                stack.append(c)
                parents[c] = start

    return parents

li = dfs(parents, stack)
for i in range(2, n+1):
    print(li[i])


