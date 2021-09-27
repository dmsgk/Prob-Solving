def solution(sizes):
    max_v, max_h = 0, 0
    for v, h in sizes:
        if v < h:
            v, h = h, v

        if v > max_v:
            max_v = v
        if h > max_h:
            max_h = h

    return max_h * max_v