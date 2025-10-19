from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        original, cnt = True, 0
        for i in nums:
            if i == 0 and original:
                cnt = cnt + 1
                original = False
            if i == 1 and original == False:
                cnt = cnt + 1
                original = True
        return cnt

