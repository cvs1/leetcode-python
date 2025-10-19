from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        integer_occurence = {}

        for num in arr:
            integer_occurence[num] = integer_occurence.get(num, 0) + 1

        res_set = set(integer_occurence.values())

        return len(integer_occurence) == len(res_set)


print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
