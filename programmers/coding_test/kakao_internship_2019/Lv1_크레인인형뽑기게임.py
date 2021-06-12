# 크레인 인형뽑기 게임
# 40분걸림.

def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        i, j = 0, m-1
        while i < len(board) and board[i][j] == 0:
            i += 1
        if i == len(board):
            continue

        if not basket:
            basket = [board[i][j]]
            board[i][j] = 0
        else:
            doll = basket.pop()
            if doll != board[i][j]:
                basket.append(doll)
                basket.append(board[i][j])
                board[i][j] = 0
            else:
                answer += 2
                board[i][j] = 0
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))  # 4