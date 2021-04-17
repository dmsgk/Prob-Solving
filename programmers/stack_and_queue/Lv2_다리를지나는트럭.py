from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    on_bridge = deque([[truck_weights.popleft(), 1]])
    cnt = 1

    while on_bridge:
        cnt += 1
        if cnt - on_bridge[0][1] == bridge_length:
            on_bridge.popleft()
            if not on_bridge and len(truck_weights) < 1:
                return cnt

        if truck_weights:
            t= truck_weights.popleft()
            if t + sum([on_bridge[i][0] for i in range(len(on_bridge))]) <= weight:
                on_bridge.append([t, cnt])
            else:
                truck_weights.appendleft(t)
    return cnt


# print(solution(100, 100, [10]))  # 101
print(solution(	2, 10, [7, 4, 5, 6]))  #8