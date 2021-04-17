from collections import deque

def solution(n, lost, reserve):
    # 리스트표현식으로 pythonic하게 풀기
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    d = deque(_reserve)

    while d and _lost:
        r = d.popleft()
        if r-1 in _lost:
            _lost.remove(r - 1)
        elif r+1 in _lost:
            _lost.remove(r + 1)
    return n - len(_lost)


print(solution(3 ,[3], [1]))   # 2