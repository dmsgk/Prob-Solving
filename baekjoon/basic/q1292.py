a, b = map(int, input().split())
li = []
i = 1
while True:
    if (i*(i+1)/2) <= b <(i+1)*(i+2)/2:
        for j in range(1,i+1):
            for _ in range(j):
                li.append(j)

        if len(li) < b:
            c = b- len(li)
            for _ in range(c):
                li.append(i+1)
        break
    i+=1

print(sum(li[a-1:]))