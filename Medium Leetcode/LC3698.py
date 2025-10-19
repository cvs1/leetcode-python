from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        left_pointer, left_sum = 0, 0
        right_pointer, right_sum = len(nums) - 1, 0

        while left_pointer != len(nums) - 1 and nums[left_pointer] < nums[left_pointer + 1]:
            left_sum += nums[left_pointer]
            left_pointer += 1

        while right_pointer > 0 and nums[right_pointer - 1] > nums[right_pointer]:
            right_sum += nums[right_pointer]
            right_pointer -= 1

        if right_pointer - left_pointer not in (0, 1):
            return -1

        if right_pointer - left_pointer == 1:
            return abs(left_sum - right_sum)

        op1 = abs((left_sum + nums[left_pointer]) - right_sum)
        op2 = abs(left_sum - (nums[left_pointer] + right_sum))

        return min(op1, op2)


Solution().splitArray([1, 2, 3, 4, 5, 3, 6, 1])
