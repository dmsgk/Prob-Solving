import itertools

def solution(nums):
    answer = 0
    sum_nums = [sum(i) for i in itertools.combinations(nums, 3)]

    for num in sum_nums:
        i = 2
        cnt = 0
        while i < num:
            if num % i == 0:
                cnt += 1
            i += 1
        if cnt == 0:
            answer += 1

    return answer