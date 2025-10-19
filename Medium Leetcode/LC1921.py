from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        cnt = 0
        killed_monster = len(dist)
        for i in range(0, len(dist)):
            dist[i] -= speed[i]
            killed_monster = min(killed_monster, dist[i])
                killed_monster = i
                cnt += 1

                if cnt >= 2:
                    return 1

        least = 999999
        for j in range(0, len(dist)):
            if j != killed_monster
                if dist[j] % speed[j] <= 1:
                    least = min(least + (dist[j] % speed[j]), dist[j] // speed[j])

        if least != 999999: return 1
        return least + cnt


Solution().eliminateMaximum([1, 3, 4], [1, 1, 1])
