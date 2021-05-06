from itertools import permutations


def solution(numbers):
    answer = 0
    li = list(numbers)
    p = set()
    for i in range(1, len(li)+1):
        p.update(list(map("".join, permutations(li, i))))
    p = set(map(int, p))

    for num in p:
        if num > 1:
            i = 2
            while i < num:
                if num % i == 0:
                    break
                i += 1
            if i == num:
                answer += 1
    return answer

print(solution("17"))
print(solution("011"))