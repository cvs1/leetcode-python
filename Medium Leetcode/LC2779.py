from collections import defaultdict
from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        slices = defaultdict(int)



        for i in nums:
            slices[i] += 1

        print(slices)





result = Solution().maximumBeauty([1, 2, 3, 4, 4], 2)
print(result)
