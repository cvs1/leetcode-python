from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        slices_lengths, cnt = [], 0
        if len(nums) < 3: return cnt

        diff = nums[1] - nums[0]

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                cnt += 1
            else:
                slices_lengths.append(cnt)
                cnt = 0
                diff = nums[i] - nums[i - 1]

        slices_lengths.append(cnt)

        total = 0

        for slices_length in slices_lengths:
            perm = slices_length * (slices_length + 1) // 2

            total += perm

        return total


Solution().numberOfArithmeticSlices([1, 2, 3, 8, 9, 10])
