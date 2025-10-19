from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        res = []

        freq_mapping = {}

        for num in nums:
            freq_mapping[num] = freq_mapping.get(num, 0) + 1

        while len(freq_mapping.items()) > 0:
            new_row = []
            for key, value in freq_mapping.items():
                new_row.append(key)
                freq_mapping[key] -= 1

            res.append(new_row)

            keys_to_remove = [key for key, value in freq_mapping.items() if value == 0]
            for key in keys_to_remove:
                freq_mapping.pop(key)

        return res


print(Solution().findMatrix([1, 1, 2, 2, 3, 3]))
