from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        diff_y_count = {}

        for coordinate in points:
            diff_y_count[coordinate[1]] = diff_y_count.get(coordinate[1], 0) + 1

        sum = 0

        for key in diff_y_count:
            diff_y_count[key] = ((diff_y_count[key] - 1) * diff_y_count[key]) // 2

        sorted_dict = dict(sorted(diff_y_count.items(), key=lambda item: item[0], reverse=True))

        for value in sorted_dict.values():
            sum += value

        sol = 0
        top_to_bottom_sum = 0
        for value in sorted_dict.values():
            top_to_bottom_sum += value
            sol += value * (sum - top_to_bottom_sum)

        return sol % (10 ** 9 + 7)


print(Solution().countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
