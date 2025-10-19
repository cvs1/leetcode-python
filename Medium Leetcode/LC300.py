from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 1: return 1

        local_longest, global_longest, local_least, global_least = 1, 1, min(nums[0], nums[1]), 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                local_longest = 1
                local_least = min(local_least, nums[i])

            elif nums[i] > local_least:
                local_longest += 1
                global_longest = max(local_longest, global_longest)

        return global_longest


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(Solution().lengthOfLIS(nums))
