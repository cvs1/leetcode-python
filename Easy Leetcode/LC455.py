from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        cnt, j = 0, 0
        if s == [] or g == []:
            return 0
        for i in range(0, len(g)):
            while j < len(s) and s[j] < g[i]:
                if j == len(s) - 1:
                    return cnt
                j += 1

            j += 1
            cnt += 1
            if j == len(s):
                return cnt

        return cnt


print(Solution().findContentChildren([1, 2, 3], [3]))
