from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        if c < 2:
            continue
        counter = Counter()
        for ord in orders:
            ord_li = list(ord)
            ord_li.sort()
            com_li = list(combinations(ord_li, c))
            counter.update(com_li)


        result = counter.most_common(1)
        if result:
            max_order = result[0][1]

            for i in range(len(counter)):
                curr = counter.most_common()[i]
                if curr[1] < max_order or curr[1] < 2:
                    break
                most_common_comb = "".join(curr[0])
                answer.append(most_common_comb)

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))  # 	["WX", "XY"]