from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()

        prefix, suffix = set(), set()
        sum = 0
        for i in range(0, len(nums) - 1):
            sum += nums[i]
            prefix.add(sum)

        sum = 0
        for i in range(len(nums) - 1, 0, -1):
            sum += nums[i]
            suffix.add(sum)

        return len(prefix.union(suffix)) < 2 * len(nums) - 2


Solution().canPartition([1, 5, 11, 5])
