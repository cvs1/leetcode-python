from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][i] += triangle[i - 1][i - 1]

        for i in range(1, len(triangle)):
            for j in range(1, i):
                triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j], triangle[i - 1][j - 1])

        return min(triangle[-1])


Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
