# 시험감독
import math
n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

ans = n
for ai in a:
    ai -= b
    if ai > 0:
        ans += math.ceil(ai/c)

print(ans)