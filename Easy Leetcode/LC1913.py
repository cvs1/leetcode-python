from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) - 1] * nums[len(nums) - 2] - nums[1] * nums[0]


print(Solution().maxProductDifference([1, 2, 3, 4]))
