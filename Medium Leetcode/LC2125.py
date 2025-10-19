from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prev, total = 0, 0
        for floor in bank:
            ones = len(floor.replace("0", ""))
            if ones != 0:
                total += prev * ones
                prev = ones

        return total

print(Solution().numberOfBeams(["011001","000000","010100","001000"]))

