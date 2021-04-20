n = int(input())
fi =[0, 1]

if n ==0:
    print(0)
else:
    while len(fi) < n+1:
        new_fi = fi[-1] + fi[-2]
        fi.append(new_fi)

    print(fi[-1])