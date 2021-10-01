# 회의실 배정

import sys
import heapq

meeting_heap = []

n = int(sys.stdin.readline())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(meeting_heap, [end, start])


prev_end, prev_start = heapq.heappop(meeting_heap)
cnt = 1
while meeting_heap:
    end, start = heapq.heappop(meeting_heap)
    while meeting_heap and prev_end > start:
        end, start = heapq.heappop(meeting_heap)

    if prev_end <= start:
        prev_end, prev_start = end, start
        cnt += 1

print(cnt)

