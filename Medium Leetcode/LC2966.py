from typing import List

import numpy


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()
        result = []
        for i in range(1, len(nums), 3):
            if nums[i + 1] - nums[i - 1] > k:
                return []



        return numpy.array(nums).reshape((len(nums) // 3, 3))


obj = Solution()
print(obj.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
