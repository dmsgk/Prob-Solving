from collections import deque


def solution(s):
    brackets = [["(", "{", "["], [")", "}", "]"]]
    answer = 0
    d = deque(s)

    if len(d) % 2 == 1:  # 괄호 개수 홀수
        return 0

    i = 0
    while i < len(d):
        a = d.popleft()
        d.append(a)
        temp = []  # 여는 괄호 저장하는 리스트
        for idx, b in enumerate(list(d)):
            if b in brackets[0]:  # 여는 괄호
                temp.append(b)
                if idx == len(d)-1:
                    break
            else:  # 닫는 괄호
                if temp:
                    a = temp.pop()
                    if brackets[0].index(a) != brackets[1].index(b):
                        break
                    elif idx == len(d)-1 and not temp:
                        answer += 1
                else:
                    break
        i += 1

    return answer


# print(solution("[](){}"))
print(solution(	"}]()[{"))  #2
print(solution("["))  #0
# print(solution("[[[[]]"))
print(solution("(][]"))
