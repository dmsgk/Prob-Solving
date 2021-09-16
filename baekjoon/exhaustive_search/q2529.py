# 부등호

import sys

sys.setrecursionlimit(10**9)
k = int(sys.stdin.readline())
ineq_li = sys.stdin.readline().split()
visited = set()
answer = []

def solution(ineq_li, depth, temp):
    global answer
    if depth == k+1:
        answer.append(temp)
        return

    if depth == 0:
        for i in range(10):
            solution(ineq_li, 1, str(i))

    else:
        prev = int(temp[-1]) # 가장 최근의 수
        visited = set(temp)
        if ineq_li[depth-1] == '>':
            for i in range(0,prev):
                if str(i) not in visited:
                    solution(ineq_li, depth+1, temp+str(i))
        else:
            for i in range(prev+1, 10):
                if str(i) not in visited:
                    solution(ineq_li, depth+1, temp+str(i))



solution(ineq_li, 0, '')
print(answer[-1])
print(answer[0])