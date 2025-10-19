from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0

        while curr < len(nums) - 1:
            while curr < len(nums) - 1 and nums[curr] == nums[curr + 1] :
                nums.remove(nums[curr])
            curr += 1

        return len(nums)


Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
