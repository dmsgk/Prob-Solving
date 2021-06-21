# 빗물
import sys

h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

water_block = 0

for hei in range(1, h+1):
    left, right = -1, -1
    for wid in range(w):
        if blocks[wid] >= hei:
            if left == -1:
                left = wid
                right = wid
            elif left < wid:
                right = wid
                if right - left > 1:
                    water_block += right - left -1
                left = right

print(water_block)