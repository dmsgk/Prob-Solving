def solution(clothes):
    clothes_type = {}

    for i in range(len(clothes)):
        if clothes[i][-1] not in clothes_type:
            clothes_type[clothes[i][-1]] = 1

        else:
            clothes_type[clothes[i][-1]] += 1

    answer = 1
    for _, value in clothes_type.items():
        answer *= (value + 1)
    answer -= 1

    return answer