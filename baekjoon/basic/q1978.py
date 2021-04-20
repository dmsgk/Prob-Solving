n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num != 1:
        i = 2
        while True:
            if i == num:
                cnt += 1
                break
            elif num % i == 0:
                break

            i += 1
print(cnt)