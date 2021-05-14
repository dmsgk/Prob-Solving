def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        cnt = 1
        num = 1
        while num < i:
            if i%num == 0:
                cnt += 1
            num += 1

        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer