from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        for num in nums:
            sum += num

        if sum > k:
            return sum % k
        elif sum == k:
            return 0
        return sum
