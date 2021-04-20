m = int(input())
n = int(input())

li = []
for num in range(m, n+1):  # m이상 n이하 자연수 각각 소수인지 체크
    if num != 1:
        i = 2
        while True:
            if i == num:
                li.append(num)
                break
            elif num % i == 0:
                break
            i += 1

li.sort()
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])