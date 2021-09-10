# 30
from collections import Counter
import operator

def solution(str_n):
    char_li = list(map(int, list(str_n)))
    char_dict = dict(Counter(char_li))
    if sum(char_li) % 3 != 0:  # 3의 배수가 될 수 없음
        return -1
    if 0 not in char_dict:
        return -1

    # key값을 기준으로 정렬.
    ans = ''
    sorted_arr = sorted(char_dict.items(), key = operator.itemgetter(0), reverse = True)
    for item in sorted_arr:
        k, v = item
        ans += str(k) * v

    return ans


str_n = input().rstrip()
print(solution(str_n))
