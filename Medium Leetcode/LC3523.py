from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:

        upto_max, max_possible = nums[0], 0

        for num in nums:
            if num >= upto_max:
                max_possible += 1
                upto_max = num

        return max_possible



print(Solution().maximumPossibleSize([4,2,5,3,5]))