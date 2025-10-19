from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for i in range(0, )


Solution().getSumAbsoluteDifferences([12, 2])
