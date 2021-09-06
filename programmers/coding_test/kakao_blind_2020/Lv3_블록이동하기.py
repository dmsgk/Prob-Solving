from collections import deque


def solution(board):
    answer = 0
    n = len(board)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
    queue = deque([((0, 0), (0, 1), 0)])
    visited = {((0, 0), (0, 1))}
    while queue:
        current = queue.popleft()
        first, second, cnt = current
        if first == (n-1, n-1) or second == (n-1, n-1):
            return cnt

        fx, fy = first
        sx, sy = second

        for i in range(4):
            nfx, nfy = fx + dx[i], fy + dy[i]
            nsx, nsy = sx + dx[i], sy + dy[i]

            if 0 <= nfx < n and 0 <= nfy < n and 0 <= nsx < n and 0 <= nsy < n and board[nfx][nfy] == 0 and board[nsx][nsy] == 0:
                if ((nfx, nfy), (nsx, nsy)) not in visited:
                    visited.add(((nfx, nfy), (nsx, nsy)))
                    queue.append(((nfx, nfy), (nsx, nsy), cnt + 1))

                if fx == sx and i >= 2:
                    continue
                if fy == sy and i < 2:
                    continue
                fir_block, sec_block = [(nfx, nfy), (fx, fy)], [(nsx, nsy), (sx, sy)]  # 첫 번째, 두번째 블럭 기준으로 회전
                fir_block.sort()
                sec_block.sort()
                fir_tup = tuple(fir_block)
                sec_tup = tuple(sec_block)

                if fir_tup not in visited:
                    visited.add(fir_tup)
                    fir_block.append(cnt+1)
                    queue.append(fir_block)

                if sec_tup not in visited:
                    visited.add(sec_tup)
                    sec_block.append(cnt+1)
                    queue.append(sec_block)

    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))  # 7
