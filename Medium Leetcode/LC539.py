from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        sorted_timePoints = sorted(timePoints, key=lambda x: (int(x.split(":")[0]), int(x.split(":")[1])))
        ans, diff = 391, 0

        for i in range(1, len(sorted_timePoints)):
            if sorted_timePoints[i - 1].split(":")[0] == sorted_timePoints[i].split(":")[0]:
                diff = int(sorted_timePoints[i].split(":")[1]) - int(sorted_timePoints[i - 1].split(":")[1])
            if int(sorted_timePoints[i - 1].split(":")[0]) == int(sorted_timePoints[i].split(":")[0]) + 1 or (
                    int(sorted_timePoints[i].split(":")[0]) == 23 and int(sorted_timePoints[i - 1].split(":")[0]) == 0):
                diff = (60 - int(sorted_timePoints[i - 1].split(":")[1])) + int(sorted_timePoints[i].split(":")[1])
            else:
                diff = (int(sorted_timePoints[i].split(":")[0]) - int(
                    sorted_timePoints[i - 1].split(":")[0]) - 1) * 60 + (
                               60 - int(sorted_timePoints[i - 1].split(":")[1])) + int(
                    sorted_timePoints[i].split(":")[1])

            ans = min(diff, ans)

        return ans
