from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        least = 200
        for task in tasks:
            least = min(task[0] + task[1], least)

        return least

