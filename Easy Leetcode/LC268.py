from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        low = 0
        hi = len(nums)

        while low < hi:

            mid = low + (hi - low) // 2

            if nums[mid] != mid:
                hi = mid
            else:
                low = mid + 1

        return low


Solution().missingNumber([0, 1])
# length = 45, missing number = 13)
