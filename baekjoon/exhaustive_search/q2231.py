# 분해합

import sys

n = int(sys.stdin.readline())


def find_num(n):
    m = 1
    while m <= n:
        sum_nums = m + sum(map(int, list(str(m))))
        if sum_nums == n:
            return m
        m += 1
    return 0


print(find_num(n))
# 245 : 256 의 생성자가 된다. (245 + 2 + 4+ 5)
# n의 가장 작은 생성자를 구하는 프로그램을 작성하시오.
