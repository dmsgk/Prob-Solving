from collections import deque
import sys


def solution(routes):
    answer = 0
    routes.sort(key=lambda start: start[0])
    routes = deque(routes)

    min_end = sys.maxsize
    while routes:
        s, e = routes.popleft()
        if not routes:
            answer += 1
        elif s <= min_end:
            min_end = min(min_end, e)
            if routes[0][0] > min_end:
                answer += 1
                min_end = routes[0][1]
    return answer


# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))  #2
# print(solution([[-2,-1], [1,2],[-3,0]])) #2
# print(solution([[0,0],])) #1
# print(solution([[0,1], [0,1], [1,2]])) #1
# print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2

