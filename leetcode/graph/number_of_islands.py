# 200. Number of Islands
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []

        def dfs(grid, start):
            grid[start[0]][start[1]] = "0"
            i, j = stack.pop()
            di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
            for idx in range(4):
                ni, nj = i + di[idx], j + dj[idx]
                if 0<= ni < m and 0<= nj < n and grid[ni][nj] == "1":
                    stack.append([ni, nj])
                    dfs(grid, [ni, nj])

        cnt = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):  # 행의 개수
            for j in range(n):  # 열 순회
                if grid[i][j] == "1":
                    stack.append([i,j])
                    dfs(grid, [i,j])
                    cnt += 1

        return cnt


test = Solution()
print(test.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))   # 1 출력