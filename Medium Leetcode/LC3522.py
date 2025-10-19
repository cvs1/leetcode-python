from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:

        visited, score, position = {}, 0, 0

        while position in range(0, len(values)) and position not in visited:
            visited.add(position)
            if instructions[position] == "add":
                score += values[position]
                position += 1
            else:
                position += values[position]

        return score


print(Solution().calculateScore(["jump", "add", "add", "jump", "add", "jump"], [2, 1, 3, 1, -2, -3]))
