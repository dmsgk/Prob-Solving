def solution(n, times):
    left, right = 0, max(times) * n  # 초기값 설정(양 극단값)
    ans = max(times) * n  # 가장 오래걸리는 심사관이 n명 모두를 심사(최댓값)

    while left <= right:
        task_done = 0
        mid = (left + right) // 2
        for t in times:
            task_done += mid // t  # 각자 mid 시간동안 심사할 수 있는 사람 수 더해주기

        if task_done < n:  # 주어진 시간 내에 모두를 심사하지 못할 경우
            left = mid + 1  # left 값 mid +1로 증가시킴.
        else:
            right = mid - 1  # right를 mid-1로 감소시킴.
            if mid <= ans:
                ans = mid  # ans 저장한 값보다 작다면 ans값 업데이트

    return ans