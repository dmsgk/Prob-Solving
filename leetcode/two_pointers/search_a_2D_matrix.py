from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # 행
        n = len(matrix[0])  # 열
        row = -1

        for i in range(m):
            if target == matrix[i][n - 1]:
                return True
            elif target < matrix[i][n - 1]:
                row = i
                break
        if row == -1:
            return False

        left, right = 0, n - 2
        while left <= right:
            if matrix[row][left] == target or matrix[row][right] == target:
                return True
            else:
                left += 1
                right -= 1
        return False
