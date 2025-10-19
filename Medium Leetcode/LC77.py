from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        current_char = 0
        neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        for r in len(board):
            for c in len(board[0]):
                if board[r][c] == current_char:
                    for neighbor in neighbors:
                        if len(neighbors) > r + neighbor[0] > -1 and len(neighbors[1]) > c + neighbor[1] > -1:
                            
