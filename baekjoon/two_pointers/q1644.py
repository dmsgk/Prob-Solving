import sys
def prime_nums(n):
    p_nums=[]
    is_prime=[1 for i in range(n+1)]
    is_prime[0]=0
    is_prime[1]=0
    for i in range(2, n+1):
        if is_prime[i]==1:
            p_nums.append(i)
            for j in range(i*i, n+1, i):
                is_prime[j]=0
    return p_nums

def findSums(n):
    p_nums=prime_nums(n)
    length=len(p_nums)
    start, end =0, 0
    cnt =0
    while True:
        if sum(p_nums[start:end])>=n:
            start += 1
        elif end==length:
            break
        else:
            end+=1
        if sum(p_nums[start:end])==n:
            cnt +=1
    return cnt
n=int(sys.stdin.readline())
print(findSums(n))