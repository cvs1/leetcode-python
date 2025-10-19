from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                ncnt = 0

                # above row
                if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] in (1, 2):
                    ncnt += 1
                if row - 1 >= 0 and board[row - 1][col] in (1, 2):
                    ncnt += 1
                if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] in (1, 2):
                    ncnt += 1
                # above row

                # same row
                if col + 1 < len(board[0]) and board[row][col + 1] in (1, 2):
                    ncnt += 1
                if col - 1 >= 0 and board[row][col - 1] in (1, 2):
                    ncnt += 1
                # same row

                # below row
                if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] in (1, 2):
                    ncnt += 1
                if row + 1 < len(board) and board[row + 1][col] in (1, 2):
                    ncnt += 1
                if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] in (1, 2):
                    ncnt += 1
                # below row

                if ncnt < 2: board[row][col] = 2
                if ncnt in (2, 3): board[row][col] = 1

                if ncnt > 3:  board[row][col] = 2
                if board[row][col] == 0 and ncnt == 3: board[row][col] = 1

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == 2: board[row][col] = 0


print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
