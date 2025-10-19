from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        rest = nums[0] + nums[1]

        hi, final_rest = -1, 0
        for i in range(2, len(nums)):
            if nums[i] < rest:
                hi = nums[i]
                final_rest = rest

            rest += nums[i]


        return hi + final_rest

