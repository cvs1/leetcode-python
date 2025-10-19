from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        sum = 0
        for i in range(1, 2 * (len(piles) // 3), 2):
            sum += piles[i]

        return sum

Solution().maxCoins([9,8,7,6,5,1,2,3,4])