n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))


for m in m_list:
    left, right = 0, n-1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if m == n_list[mid]:
            print(1)
            flag = True
            break
        elif m > n_list[mid]:
            left = mid + 1
        elif m < n_list[mid]:
            right = mid - 1

    if not flag:
        print(0)