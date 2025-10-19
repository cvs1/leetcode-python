from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        cnt, upto_max = 0, weight[0]

        for i in range(0, len(weight)):
            if weight[i] < upto_max:
                cnt += 1
                if i < len(weight) - 1:
                    upto_max = weight[i + 1]


        return cnt
