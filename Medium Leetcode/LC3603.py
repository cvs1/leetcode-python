from typing import List


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:

        row, col = 0, 0

        while row < m:
            while col < n:
                waitCost[row][col] += (row + 1) * (col + 1)
                col += 1

            row += 1
            col = 0

        for j in range(2, n):
            waitCost[0][i] += waitCost[0][i - 1]

        for i in range(2, m):
            waitCost[i][0] += waitCost[i - 1][0]

        i, j = 1, 1

        while i < m:
            while j < n:
                waitCost[i][j] += min(waitCost[i][j - 1], waitCost[i - 1][j])
                j += 1

            i += 1
            j = 0

        return waitCost[m - 1][n - 1]


print(Solution().minCost(1, 2, [[6, 2]]))
