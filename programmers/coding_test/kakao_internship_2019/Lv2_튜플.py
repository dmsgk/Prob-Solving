# 튜플, 50분 걸림..

def solution(s):
    answer = []
    s = s.strip("}")
    s = s.strip("{{")
    s = s.split("},{")

    l1 = []
    for num in s:
        l1.append(list(map(int, num.split(","))))

    i = 0
    while len(answer) < len(l1):
        for k in range(len(l1)):
            if len(l1[k]) == i+1:
                for j in l1[k]:
                    if j not in answer:
                        answer.append(j)
                break
        i += 1

    return answer



print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
# print(solution("{{20,111},{111}}"))