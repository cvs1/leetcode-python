from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        h_possibles, v_possibles = set(), set()

        hFences.append(1)
        hFences.append(m)

        vFences.append(1)
        vFences.append(n)

        for i in range(0, len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_possibles.add(abs(hFences[i] - hFences[j]))

        for i in range(0, len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_possibles.add(abs(vFences[i] - vFences[j]))

        if len(h_possibles.intersection(v_possibles)) == 0:
            return -1

        return (sorted(h_possibles.intersection(v_possibles))[-1] ** 2) % (10**9 + 7)


obj = Solution()
print(obj.maximizeSquareArea(4, 3, [2, 3], [2]))
