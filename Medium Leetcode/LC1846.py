from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        myset = set()
        myset.update(arr)

        return len(myset)


print(Solution().maximumElementAfterDecrementingAndRearranging([7, 8, 9, 10]))
