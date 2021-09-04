from copy import deepcopy


def check(x, y, a, beam, column):
    if a == 0:  # 기둥
        if y == 0 or [x, y, 1] in beam or [x - 1, y, 1] in beam or [x, y-1, 0] in column:
            return True
    else:  # 보
        if [x, y - 1, 0] in column or [x + 1, y - 1, 0] in column or (
                [x - 1, y, 1] in beam and [x + 1, y, 1] in beam):
            return True
    return False


def solution(n, build_frame):
    beam, column = [], []
    for cmd in build_frame:
        x, y, a, b = cmd

        if b == 1 and check(x, y, a, beam, column):
            if a == 0:
                column.append([x, y, 0])
            else:
                beam.append([x, y, 1])
        elif b ==0:  # 삭제
            if a == 0: # 기둥
                temp_col = deepcopy(column)
                temp_col.remove([x,y,0])
                temp_result = temp_col + beam
                for cmd in temp_result:
                    x, y, a = cmd
                    if not check(x, y, a, beam, temp_col):
                        break
                else:
                    column = temp_col

            else: # 보
                temp_beam = deepcopy(beam)
                temp_beam.remove([x,y,1])
                temp_result = column + temp_beam
                for cmd in temp_result:
                    x, y, a = cmd
                    if not check(x, y, a, temp_beam, column):
                        break
                else:
                    beam = temp_beam

    answer = beam + column
    answer.sort(key= lambda idx : (idx[0], idx[1], idx[2]))
    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]