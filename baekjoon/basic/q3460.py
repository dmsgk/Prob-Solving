t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    i = 0
    while n>0:
        if n < 2**(i+1) and n>= 2**i:
            l.append(i)
            n -= 2**i
            i = -1
        i += 1
    l.reverse()

    for i in l:
        print(i, end = ' ')

    print()