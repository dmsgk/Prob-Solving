# 영화감독 숌
import sys

n = int(sys.stdin.readline())
prev = 666
num = prev
for _ in range(1, n):
    while True:
        num += 1
        if '666' in str(num):
            prev = num
            break
print(num)