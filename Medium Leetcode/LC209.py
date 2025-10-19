from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        least = 2 ** 63 - 1
        exists = False
        for i in range(0, len(nums)):
            if nums[i] >= target:
                least = i + 1
            for j in range(i - 1, -1, -1):

                if nums[i] - nums[j] >= target:
                    exists = True
                    curr = i - j

                    least = min(least, curr)

        if exists == False and nums[-1] >= target:
            return len(nums)
        if exists == False:
            return 0
        return least


print(Solution().minSubArrayLen(5, [2, 3, 1, 1, 1, 1, 1]))
