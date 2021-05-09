def solution(t, r):
    answer = []
    info = []
    for i, v in enumerate(t):
        info.append([r[i],v, i])  # 우선순위, 도착순서, 손님아이디
    info.sort()
    iteration = 0
    while info:
        i = 0
        while i<len(info)-1 and info[i][1] > iteration:
            i += 1
        if info[i][1] <= iteration:
            r, t, c = info.pop(i)
            answer.append(c)
        iteration += 1

    return answer


print(solution([0,1,3,0],[0,1,2,3]))  #[0,1,3,2]
print(solution([7, 6, 8, 1], [0, 1, 2, 3]))  #[3, 1, 0, 2]