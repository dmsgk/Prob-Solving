# 두 수의 합

n = int(input())
seq = list(map(int, input().split()))
x = int(input())

lp, rp = 0, n - 1
seq.sort()
cnt = 0

while lp < rp:
    if seq[lp] + seq[rp] > x:
        rp -= 1
    elif seq[lp] + seq[rp] == x:
        cnt += 1
        lp += 1
        rp -= 1
    else:
        lp += 1
print(cnt)



