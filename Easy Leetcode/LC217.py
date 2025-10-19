from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        uniq = {}

        for i in range(0, len(nums)):
            if nums[i] in uniq:
                return True

            uniq.add(nums[i])

        return False
