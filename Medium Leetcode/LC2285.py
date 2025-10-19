from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        freq_mapping = {key: 0 for key in range(0, n)}

        for road in roads:
            freq_mapping[road[0]] = freq_mapping.get(road[0]) + 1
            freq_mapping[road[1]] = freq_mapping.get(road[1]) + 1

        sorted_mapping = dict(sorted(freq_mapping.items(), key=lambda item: item[1]))

        res = 0
        m = 1
        for value in sorted_mapping.values():
            res += value * m
            m += 1

        return res


print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
