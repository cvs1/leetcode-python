from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_res = {}
        players = set()

        for match in matches:
            player_res[match[1]] = player_res.get(match[1], 0) + 1
            players.add(match[0])

        ans = [[], []]

        for key, value in player_res.items():
            if value == 1:
                ans[1].append(key)

        for plyr in players:
            if player_res.get(plyr, 0) == 0:
                ans[0].append(plyr)

        ans[0].sort()
        ans[1].sort()
        return ans


print(Solution().findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
