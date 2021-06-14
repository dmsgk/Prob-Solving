# 퇴사
import sys

n = int(sys.stdin.readline().strip())
task_dict = {i:list(map(int,sys.stdin.readline().strip().split())) for i in range(n)}
dp = [0] * (n+1)

def dp_task(n, task_dict, dp):
    for i in range(n):
        if i + task_dict[i][0] < n+1 :
            dp[i + task_dict[i][0]] = max(dp[i + task_dict[i][0]], task_dict[i][1] + dp[i])
        if i < n:
            dp[i + 1] = max(dp[i + 1], dp[i])


    return max(dp)

print(dp_task(n, task_dict, dp))

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

45 출력
"""