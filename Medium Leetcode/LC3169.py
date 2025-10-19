from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
        count, r_most = 0, 0
        for i in range(0, len(meetings)):
            if meetings[i][0] > r_most:
                count += meetings[i][0] - r_most - 1

            if i!=0 and meetings[i][0] > meetings[i - 1][0] and meetings[i - 1][1] > r_most:
                r_most = meetings[i - 1][1]

        return count

Solution().countDays(10, [[5,7],[1,3],[9,10]])