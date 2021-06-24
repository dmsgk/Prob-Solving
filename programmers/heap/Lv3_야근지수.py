import bisect

def solution(n, works):
    answer = 0
    works.sort()

    for _ in range(n):
        if works:
            if len(works) == 1:
                works[-1] -= 1
                if works[-1] == 0:
                    works.pop()
            else:
                right = works.pop()
                right -= 1
                if right != 0:
                    bisect.insort(works, right)

    for leftover in works:
        answer += leftover ** 2

    return answer