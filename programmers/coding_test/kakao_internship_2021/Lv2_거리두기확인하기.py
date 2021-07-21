def solution(places):
    answer = []

    # 각 대기실별로 거리두기 준수여부 체크
    for idx, room in enumerate(places):
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if not dfs(room, i, j):  # 방역수칙 위반
                        answer.append(0)
                        break
            if len(answer) == idx+1:   # 이미 방역수칙 위반해 0이 추가된 경우
                break
        else:
            answer.append(1)   # 모두 방역수칙 준수한 경우

    return answer


def dfs(room, row, col):
    dx, dy = [0, 0, 1], [-1, 1, 0]  # 좌, 우, 하 우
    stack = [[row, col, 0]]
    visited = {(row, col)}
    while stack:
        x, y, num = stack.pop()
        if num == 3:
            return True
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) not in visited:
                visited.add((nx, ny))
                if room[nx][ny] == 'P':
                    if num < 2:
                        return False
                    stack.append([nx, ny, num + 1])

                elif room[nx][ny] == 'O':
                    stack.append([nx,ny, num+1])

    return True

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))