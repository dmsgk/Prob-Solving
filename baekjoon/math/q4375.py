# 1

while 1:
    try:
        n = int(input())  # 문자열 형태로 남겨두기.
    except EOFError:
        break

    length = len(str(n))
    if str(n) > '1' * length:
        start = '1' * (length+1)
    else:
        start = '1' * length

    while 1:
        if int(start) % n == 0:
            print(len(start))
            break
        else:
            start += '1'