import math
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int):
        nums.sort()
        prefer_op1 = (math.ceil(nums[- 1] / 2) - nums[- 1] % 2) > k  # op1 then op2

        for i in range(len(nums) - 1, -1, -1):

            if prefer_op1:
                if op1 > 0:
                    r = nums[i] % 2
                    nums[i] = math.ceil(nums[i] / 2)
                    op1 -= 1

                if op2 > 0 and nums[i] >= k:
                    nums[i] -= k
                    op2 -= 1
            else:
                if op2 > 0 and nums[i] >= k:
                    nums[i] -= k
                    op2 -= 1
                if op1 > 0:
                    r = nums[i] % 2
                    nums[i] = math.ceil(nums[i] / 2)
                    op1 -= 1

        return sum(nums)


print(Solution.minArraySum([12, 3, 1, 2, 3], [2,4,3], 3, 2, 1))
