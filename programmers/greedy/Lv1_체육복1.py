from collections import deque

def solution(n, lost, reserve):
    answer = n - len(lost)

    lost.sort()
    reserve.sort()
    d = deque(reserve)
    i = 0
    while i < len(reserve):
        a = d.popleft()
        if a in lost:
            lost.remove(a)
            answer += 1
        else:
            d.append(a)
        i += 1

    while d and lost:
        r = d.popleft()
        if r-1 in lost:
            lost.remove(r-1)
            answer += 1
        elif r+1 in lost:
            lost.remove(r+1)
            answer += 1
    return answer


print(solution(3 ,[3], [1]))   # 2