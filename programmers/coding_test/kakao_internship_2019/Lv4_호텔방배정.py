def solution(k, room_number):
    result = []
    room = {i:i for i in range(k+1)}
    visited = []
    for r in room_number:
        idx = room[r]
        while idx in visited:
            room[idx] += 1
            idx = room[idx]
        visited.append(idx)
        result.append(idx)
    return result

print(solution(10, [1,3,4,1,3,1]))  # [1,3,4,2,5,6]