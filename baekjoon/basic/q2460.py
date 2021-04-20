li = []
for i in range(10):
    drop, ride = map(int, input().split())
    new = ride - drop
    if i == 0:
        li.append(ride)
    else:
        li.append(li[i-1]+ new)

print(max(li))