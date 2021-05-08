# 부분합
import sys

n, s = map(int, input().split())
arr = list(map(int,input().split()))

l, r = 0,0
temp = 0
min_length = sys.maxsize

while True:
    if temp >= s:
        min_length = min(min_length, r-l)
        temp -= arr[l]
        l += 1
    elif r == n:
        break
    else:
        temp += arr[r]
        r += 1
if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)

"""
10 15
5 1 3 5 10 7 4 9 2 8
"""

