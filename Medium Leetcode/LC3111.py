from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        sorted_cordinates = sorted(points, key=lambda x: x[0])
        prev, cnt = sorted_cordinates[0][0], 1
        for cordinate in sorted_cordinates:
            if not cordinate[0] <= prev + w:
                cnt += 1
                prev = cordinate[0]

        return cnt
