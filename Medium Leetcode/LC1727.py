from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        for row in range(1, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] != 0:
                    matrix[row][col] += matrix[row - 1][col]
                    
