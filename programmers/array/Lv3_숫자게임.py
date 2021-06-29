def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(B)):
        if A[i] < B[i]:
            answer += 1
        else:
            A_maxnum = A.pop()
            A.insert(i, A_maxnum)

    return answer