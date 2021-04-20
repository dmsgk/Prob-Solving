import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    days = deque()
    progresses = deque(progresses)
    speeds = deque(speeds)

    while speeds:
        s, p = speeds.popleft(), progresses.popleft()
        left = 100- p
        days.append(math.ceil(left /s))
    print(days)
    cnt = 1
    while len(days) > 1:
        d = days.popleft()
        while days and d >= days[0]:
            days.popleft()
            cnt += 1
        answer.append(cnt)
        cnt = 1
    if days:
        answer.append(1)

    return answer


print(solution(	[93, 30, 55], [1, 30, 5])) #[2,1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))   # 	[1, 3, 2]
print(solution([96, 99, 98, 97], [1, 1, 1, 1] ))  #[4]