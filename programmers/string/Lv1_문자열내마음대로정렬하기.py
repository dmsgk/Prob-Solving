def solution(strings, n):
    answer = sorted(strings, key = lambda idx : idx[n])
    return answer



print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
