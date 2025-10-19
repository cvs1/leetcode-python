from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        diff, cnt, max_freq = 0, 0, 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] + diff <= k:
                cnt += 1
                diff += nums[i] - nums[i - 1]
            else:
                max_freq = max(cnt, max_freq)
                cnt = 0
                diff = 0

        return max(cnt, max_freq) + 1


print(Solution().maxFrequency([1,4,8,13], 5))
