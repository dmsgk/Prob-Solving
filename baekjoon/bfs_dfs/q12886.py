# 돌 그룹
import sys
from collections import deque

a, b, c = map(int, sys.stdin.readline().split())


def solution(a, b, c):
    total_stone = a + b + c
    if total_stone % 3 != 0:
        return 0

    max_num = max(a, max(b,c))
    min_num = min(a, min(b,c))
    other = total_stone - min_num - max_num

    queue = deque([(min_num, other, max_num)])  # 현재상태
    visited = {(min_num, other, max_num)}
    while queue:
        q = queue.popleft()
        if len(set(q)) == 1:
            return 1
        x, y, z = q
        if x < y:
            min_num, leftover, max_num = sort_stones(x, y, z)

            if (min_num, leftover, max_num) not in visited:
                visited.add((min_num, leftover, max_num))
                queue.append((min_num, leftover, max_num))
        if y < z:
            min_num, leftover, max_num = sort_stones(y, z, x)
            if (min_num, leftover, max_num) not in visited:
                visited.add((min_num, leftover, max_num))
                queue.append((min_num, leftover, max_num))
        if x < z:
            min_num, leftover, max_num = sort_stones(x, z, y)
            if (min_num, leftover, max_num) not in visited:
                visited.add((min_num, leftover, max_num))
                queue.append((min_num, leftover, max_num))
    return 0


def sort_stones(small, large, other):
    total_stone = small + large + other
    max_num = max(2 * small, max(large-small, other))
    min_num = min(2 * small, min(large-small, other))
    leftover = total_stone - min_num - max_num
    return min_num, leftover, max_num

print(solution(a,b,c))