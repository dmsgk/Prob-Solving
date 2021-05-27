import collections

def solution(numbers, target):
    q_nums = collections.deque(numbers)
    visited = []
    while q_nums:
        temp = []
        num = q_nums.popleft()
        if not visited:
            visited = [-num, +num]
            continue
        for i in visited:
            temp += [i+num, i-num]
        visited = temp

    d = dict(collections.Counter(visited))
    return d[target]

print(solution([1, 1, 1, 1, 1],	3))  # 5