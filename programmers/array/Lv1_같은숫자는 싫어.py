def solution(arr):
    answer = []
    for num in arr:
        if not answer:
            answer = [num]
        else:
            last_num = answer.pop()
            if num != last_num:
                answer.append(last_num)
            answer.append(num)

    return answer