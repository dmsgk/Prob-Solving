# 연결 요소의 개수
n, m = map(int, input().split())
linked = {i: set() for i in range(1, n+1)}

for _ in range(m):
    i, j = map(int, input().split())
    linked[i].add(j)
    linked[j].add(i)

visited = set()
stack = [1]
result = 0
node = set(i for i in range(1, n+1))


while stack:
    num = stack.pop()
    visited.add(num)
    li = list((linked[num]-visited)-set(stack))
    stack += li

    if not stack:
        result += 1
        node -= visited
        if node:
            stack.append(node.pop())

print(result)