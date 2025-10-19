from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            if value > len(nums) // 3:
                res.append(key)

        return res
