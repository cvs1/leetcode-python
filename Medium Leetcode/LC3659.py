from collections import defaultdict
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        m = len(nums) // k
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        for val in freq.values():
            if val > m:
                return False

        return True
