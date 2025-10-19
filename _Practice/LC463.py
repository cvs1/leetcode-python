from cmath import inf
from typing import List


class Solution:
    def minArraySum(self, A: List[int], k: int) -> int:
        dp = [0] + [inf] * k

        res = 0
w        for a in A:
            res += a
            res = dp[res % k] = min(dp[res % k], res)

        return res


print(Solution().minArraySum([3, 1, 4, 1, 5], 3))
