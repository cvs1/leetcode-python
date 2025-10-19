from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        prev, rep = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev + maxDiff:
                prev = nums[i]
                nums[i] = rep
            else:
                rep = nums[i]
                prev = nums[i]

        res = [False] * len(queries)
        i = 0
        for query in queries:

            if nums[query[0]] == nums[query[1]]:
                res[i] = True
            i += 1

        return res


print(Solution().pathExistenceQueries(4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]))
