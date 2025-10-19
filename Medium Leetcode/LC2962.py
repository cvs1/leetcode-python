from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        indices = []
        highest = 0

        for i in range(0, len(nums)):
            if nums[i] > highest:
                indices.clear()
                highest = nums[i]
                indices.append(i)
            elif nums[i] == highest:
                indices.append(i)

        if len(indices) < k:
            return 0

        l = indices[0]
        r = len(nums) - indices[k - 1]
        cnt = (l + 1) * r
        for ind in range(1, len(indices) - k + 1):
            l = indices[ind] - indices[ind - 1]
            r = len(nums) - indices[ind + k - 1]
            cnt += l * r

        return cnt


obj = Solution()
print(obj.countSubarrays([1, 3, 2, 3, 3], 2))
