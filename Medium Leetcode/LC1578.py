from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sum, local_min, res, flag = 0, 0, 0, False
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                flag = True
                local_min = min(neededTime[i - 1], neededTime[i])
                neededTime[i] = local_min
            elif flag:
                flag = False
                res += local_min
                local_min = 0

        return res + local_min