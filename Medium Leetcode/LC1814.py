from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        reverse_diff, nice_pairs = {}, 0

        for num in nums:
            reverse_diff[num - int(str(num)[::-1])] = reverse_diff.get(num - int(str(num)[::-1]), 0) + 1

        for value in reverse_diff.values():
            nice_pairs += ((value - 1) * value) / 2

        return int(nice_pairs) % (10 ** 9 + 7)

nums = [13,10,35,24,76]
print(Solution().countNicePairs(nums))
