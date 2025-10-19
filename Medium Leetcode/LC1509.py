from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return 0 if len(nums) <= 3 else min(nums[::-1][3] - nums[0], nums[-1] - nums[3])


print(Solution().minDifference([4, 1, 7, 2, 3]))
