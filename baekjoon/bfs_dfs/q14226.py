# 이모티콘
# bfs를 사용할 때는 종속적이지 않은 변수를 큐에 넣을 때는 방문체크 역시 각각을 별개의 차원으로 놓고 풀기!!
import sys
from collections import deque

s = int(sys.stdin.readline())


def bfs(s):
    clip_board = 0
    queue = deque([[1, clip_board, 0]])  # 현재 화면에 있는 이모지수, 클립보드에 복사된 수, 현재 횟수
    visited = {(1,0)}

    while queue:
        curr, clip_board, cnt = queue.popleft()

        if curr == s:
            return cnt

        if clip_board > 0 and (curr+clip_board, clip_board) not in visited:
            visited.add((curr+clip_board, clip_board))
            queue.append([curr+clip_board, clip_board, cnt+1])  # 붙여넣기
        if curr > 0:
            queue.append([curr, curr, cnt+1])  # 복사
            if (curr-1, clip_board) not in visited:
                visited.add((curr-1, clip_board))
                queue.append([curr-1, clip_board, cnt + 1])  # 지우기

print(bfs(s))