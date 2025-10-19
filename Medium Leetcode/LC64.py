from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        for j in range(1, len(grid)):
            grid[j][0] += grid[j - 1][0]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

        return grid[len(grid) - 1][len(grid[0]) - 1]
