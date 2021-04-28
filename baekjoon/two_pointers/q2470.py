# 두 용액

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = {}

lp, rp = 0, n-1
while lp < rp:
    if abs(arr[rp]+arr[lp]) not in answer:
        answer[abs(arr[rp]+arr[lp])] = [arr[lp], arr[rp]]

    if abs(arr[lp])> abs(arr[rp]):
        lp += 1
    else:
        rp -= 1

ans = answer[min(answer)]
print( " ".join(list(map(str, ans))))