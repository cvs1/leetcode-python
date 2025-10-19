from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        freq, operations = {}, 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for value in freq.values():
            if value == 1:
                return -1
            if value == 2:
                operations += 1
            elif value % 3 == 0:
                operations += (value // 3)
            else:
                operations += (value // 3) + 1

        return operations


nums = [2,1,2,2,3,3]
print(Solution().minOperations(nums))
