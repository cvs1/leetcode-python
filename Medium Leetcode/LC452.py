from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sortedArrows = sorted(points, key=lambda x: (x[0], x[1]))

        last, cnt = sortedArrows[0][1], 1
        left, right  = sortedArrows[0][0], sortedArrows[0][1]
        for i in range(1, len(sortedArrows)):


            left, right = sortedArrows[i][0], sortedArrows[i][1]

            if sortedArrows[i][0] > last:
                cnt += 1
            last = sortedArrows[i][1]

        return cnt


print(Solution().findMinArrowShots([[1, 6], [1, 2], [1, 3], [1, 1]]))
