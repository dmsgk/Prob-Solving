# 후보 추천하기

import sys
import operator

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
std_li = list(map(int, sys.stdin.readline().strip().split()))

def solution(std_li):
    std_dict = {}  # 각 사진첩을 key로 하는 딕셔너리 생성
    for std in std_li:
        if std not in std_dict:
            if len(std_dict) >= n:   # 사진첩에 자리가 없는 경우.
                sorted_arr = sorted(std_dict.items(), key=operator.itemgetter(1)) # value 기준으로 역순 정렬
                delkey = sorted_arr[0][0]
                del std_dict[delkey]
            std_dict[std] = 1
        else:
            std_dict[std] += 1  # 추천수만 1증가시킴.
    ans = []
    sorted_arr = sorted(std_dict.items())
    for s in sorted_arr:
        ans.append(s[0])

    return " ".join(list(map(str, ans)))

print(solution(std_li))