n, m = map(int, input().split())

num = min(n,m)
while num >0:
    if n % num == 0 and m % num == 0:
        print(num)
        break
    num -= 1

num = min(n,m)
num1 = max(n,m)
i = 1
while True:
    if (num1 * i) % num == 0:
        print(num1*i)
        break
    i+= 1